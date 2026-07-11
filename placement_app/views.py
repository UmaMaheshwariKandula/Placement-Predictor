import json
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from .models import Profile, StudentRecord, MockTest, MockTestQuestion, MockTestResult
from .serializers import StudentRecordSerializer
from .utils import (
    analyze_github_profile,
    score_resume,
    get_company_matches,
    analyze_skill_gap,
    predict_placement,
    predict_timeline,
    COMPANIES,
    verify_hackerrank,
    verify_leetcode,
    check_data_consistency,
    calculate_improvement_impact,
    predict_salary,
)


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "placement_app/login.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        role = request.POST.get("role")
        if form.is_valid() and role in ["student", "faculty", "officer"]:
            user = form.save()
            Profile.objects.create(user=user, role=role)
            messages.success(request, "Registration successful. Please log in.")
            return redirect("login")
        messages.error(request, "Please correct the errors and choose a role.")
    else:
        form = UserCreationForm()
    return render(request, "placement_app/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile, created = Profile.objects.get_or_create(user=user, defaults={'role': 'student'})
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, "placement_app/login.html", {"form": form, "register": False})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard_view(request):
    profile = getattr(request.user, "profile", None)
    if profile is None:
        return redirect("logout")
    if profile.role == "student":
        return redirect("student_dashboard")
    if profile.role == "faculty":
        return redirect("faculty_dashboard")
    return redirect("officer_dashboard")


@login_required
def student_dashboard(request):
    profile = getattr(request.user, "profile", None)
    if not profile or profile.role != "student":
        return redirect("dashboard")
    student_records = StudentRecord.objects.filter(user=request.user).order_by("-created_at")[:5]
    
    trending_skills = [
        {"skill": "🐍 Python", "demand": 95, "salary": "₹12L"},
        {"skill": "🤖 Machine Learning", "demand": 92, "salary": "₹15L"},
        {"skill": "☁️ Cloud Computing", "demand": 90, "salary": "₹14L"},
        {"skill": "📊 Data Science", "demand": 88, "salary": "₹13L"},
        {"skill": "🧠 Artificial Intelligence", "demand": 85, "salary": "₹16L"},
        {"skill": "🌐 Full Stack Development", "demand": 82, "salary": "₹11L"},
        {"skill": "🔒 Cybersecurity", "demand": 80, "salary": "₹12L"},
        {"skill": "⚙️ DevOps", "demand": 78, "salary": "₹13L"},
        {"skill": "🗄️ SQL", "demand": 75, "salary": "₹9L"},
        {"skill": "☕ Java", "demand": 73, "salary": "₹10L"},
        {"skill": "⚛️ React.js", "demand": 70, "salary": "₹10L"},
        {"skill": "🟢 Node.js", "demand": 68, "salary": "₹9L"},
        {"skill": "🐳 Docker", "demand": 65, "salary": "₹11L"},
        {"skill": "☸️ Kubernetes", "demand": 62, "salary": "₹12L"},
        {"skill": "📦 AWS", "demand": 60, "salary": "₹13L"},
        {"skill": "🔷 Azure", "demand": 58, "salary": "₹12L"},
        {"skill": "📈 Power BI", "demand": 55, "salary": "₹8L"},
        {"skill": "📊 Tableau", "demand": 53, "salary": "₹9L"},
        {"skill": "📑 Excel", "demand": 50, "salary": "₹7L"},
        {"skill": "🐘 PHP", "demand": 48, "salary": "₹8L"},
        {"skill": "🎨 UI/UX Design", "demand": 45, "salary": "₹9L"},
        {"skill": "📱 Android Development", "demand": 42, "salary": "₹10L"},
        {"skill": "🍏 iOS Development", "demand": 40, "salary": "₹11L"},
        {"skill": "🎮 Game Development", "demand": 38, "salary": "₹9L"},
        {"skill": "🔗 Blockchain", "demand": 35, "salary": "₹18L"},
    ]
    
    predictions = {}
    resume_result = {}
    github_result = {}
    company_matches = []
    skill_analysis = {}
    data_warnings = []
    timeline = {"predicted_month": 6, "distribution": [8.33] * 12}
    salary_prediction = None
    
    # Initialize improvement_impacts with sample data so it shows immediately
    improvement_impacts = {
        'current_probability': 59.4,
        'potential_probability': 78.0,
        'total_improvement': 18.6,
        'impacts': [
            {'skill': 'Coding Score', 'current': 70, 'target': 80, 'improvement': '+10 points', 'impact': '+9.0%', 'tip': 'Practice coding daily on HackerRank or LeetCode'},
            {'skill': 'CGPA', 'current': 7.0, 'target': 7.5, 'improvement': '+0.5 points', 'impact': '+5.0%', 'tip': 'Focus on subjects with low grades, attend extra classes'},
            {'skill': 'Projects', 'current': 2, 'target': 4, 'improvement': '+2 projects', 'impact': '+3.0%', 'tip': 'Build 2 new projects using your skills'},
            {'skill': 'Aptitude Score', 'current': 65, 'target': 75, 'improvement': '+10 points', 'impact': '+1.5%', 'tip': 'Solve 10 aptitude questions daily from Indiabix'},
        ]
    }
    
    if request.method == "POST":
        payload = {
            "cgpa": float(request.POST.get("cgpa", 0)),
            "backlogs": int(request.POST.get("backlogs", 0)),
            "coding_score": int(request.POST.get("coding_score", 0)),
            "aptitude_score": int(request.POST.get("aptitude_score", 0)),
            "communication_score": int(request.POST.get("communication_score", 0)),
            "projects": int(request.POST.get("projects", 0)),
            "internships": int(request.POST.get("internships", 0)),
            "certifications": int(request.POST.get("certifications", 0)),
            "github_contributions": int(request.POST.get("github_contributions", 0)),
            "leetcode_solved": int(request.POST.get("leetcode_solved", 0)),
            "hackathon": int(request.POST.get("hackathon", 0)),
            "soft_skills": int(request.POST.get("soft_skills", 0)),
            "extra_skills": request.POST.get("extra_skills", ""),
        }
        
        # Check data consistency
        data_warnings = check_data_consistency(payload)
        
        github_username = request.POST.get("github_username", "")
        if github_username:
            github_result = analyze_github_profile(github_username)
            payload["github_contributions"] = github_result.get("commits", payload["github_contributions"])
            if github_result.get('verified'):
                data_warnings.append("✅ GitHub profile verified - data is authentic")
        
        if request.FILES.get("resume_file"):
            resume_result = score_resume(request.FILES["resume_file"])
            payload["resume_score"] = resume_result.get("resume_score", 0)
        
        predictions = predict_placement(payload)
        
        # Calculate salary prediction
        salary_prediction = predict_salary(payload)
        
        # Update improvement_impacts with REAL data from the form
        improvement_impacts = calculate_improvement_impact(payload)
        
        timeline = predict_timeline(payload)
        company_matches = get_company_matches(payload)
        skill_analysis = analyze_skill_gap(payload)
        placement_probability = predictions.get("average_probability", 0.0)
        
        StudentRecord.objects.create(
            user=request.user,
            cgpa=payload["cgpa"],
            backlogs=payload["backlogs"],
            coding_score=payload["coding_score"],
            aptitude_score=payload["aptitude_score"],
            communication_score=payload["communication_score"],
            projects=payload["projects"],
            internships=payload["internships"],
            certifications=payload["certifications"],
            github_contributions=payload["github_contributions"],
            leetcode_solved=payload["leetcode_solved"],
            hackathon=payload["hackathon"],
            soft_skills=payload["soft_skills"],
            resume_score=resume_result.get("resume_score", 0),
            github_score=github_result.get("developer_score", 0),
            placement_probability=placement_probability,
            placement_month=timeline.get("predicted_month", 6),
            company_matches=company_matches,
            skill_gaps=skill_analysis.get("skill_gaps", []),
        )
        student_records = StudentRecord.objects.filter(user=request.user).order_by("-created_at")[:5]
        messages.success(request, "Prediction generated successfully.")
    
    return render(request, "placement_app/student_dashboard.html", {
        "student_records": student_records,
        "predictions": predictions,
        "resume_result": resume_result,
        "github_result": github_result,
        "company_matches": company_matches,
        "skill_analysis": skill_analysis,
        "trending_skills": trending_skills,
        "timeline": timeline,
        "data_warnings": data_warnings,
        "improvement_impacts": improvement_impacts,
        "salary_prediction": salary_prediction,
    })


@login_required
def faculty_dashboard(request):
    profile = getattr(request.user, "profile", None)
    if not profile or profile.role != "faculty":
        return redirect("dashboard")
    records = StudentRecord.objects.order_by("-created_at")[:50]
    probabilities = [r.placement_probability for r in records]
    average_probability = round(sum(probabilities) / len(probabilities), 2) if probabilities else 0
    at_risk = [r for r in records if r.placement_probability < 30]
    top_students = sorted(records, key=lambda r: r.placement_probability, reverse=True)[:5]
    skill_trends = []
    for r in records[:10]:
        skill_trends.append({
            "id": r.id,
            "name": r.user.username if r.user else f"Guest-{r.id}",
            "gap_count": len(r.skill_gaps),
            "probability": r.placement_probability,
        })
    return render(request, "placement_app/faculty_dashboard.html", {
        "records": records,
        "average_probability": average_probability,
        "at_risk": at_risk,
        "top_students": top_students,
        "skill_trends": skill_trends,
    })


@login_required
def officer_dashboard(request):
    profile = getattr(request.user, "profile", None)
    if not profile or profile.role != "officer":
        return redirect("dashboard")
    records = StudentRecord.objects.order_by("-created_at")[:100]
    total = len(records)
    placed_count = len([r for r in records if r.placement_probability >= 50])
    placement_rate = round((placed_count / total * 100), 2) if total else 0
    companies = {}
    for company in COMPANIES[:10]:
        companies[company["name"]] = companies.get(company["name"], 0) + 1
    demand_heatmap = [
        {"skill": "Python", "value": 95},
        {"skill": "Data Science", "value": 88},
        {"skill": "Cloud", "value": 80},
        {"skill": "Fullstack", "value": 78},
    ]
    batch_comparison = {
        "current_batch": round(placement_rate, 2),
        "previous_batch": round(max(0, placement_rate - 8), 2),
    }
    return render(request, "placement_app/admin_dashboard.html", {
        "total": total,
        "placement_rate": placement_rate,
        "company_counts": companies,
        "demand_heatmap": demand_heatmap,
        "batch_comparison": batch_comparison,
    })


@login_required
def download_report(request, pk):
    record = get_object_or_404(StudentRecord, pk=pk)
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f"attachment; filename=placement_report_{record.id}.pdf"
    buffer = canvas.Canvas(response, pagesize=letter)
    buffer.setFont("Helvetica-Bold", 16)
    buffer.drawString(50, 750, "Placement Success Prediction Report")
    buffer.setFont("Helvetica", 11)
    buffer.drawString(50, 720, f"Student: {record.user.username if record.user else 'Guest'}")
    buffer.drawString(50, 700, f"Prediction probability: {record.placement_probability}%")
    buffer.drawString(50, 680, f"Predicted placement month: {record.placement_month}")
    buffer.drawString(50, 660, f"Resume score: {record.resume_score}")
    buffer.drawString(50, 640, f"GitHub score: {record.github_score}")
    buffer.drawString(50, 620, "Top company matches:")
    offset = 600
    for match in record.company_matches[:5]:
        buffer.drawString(60, offset, f"{match['company']}: {match['match_percentage']}%")
        offset -= 20
    buffer.drawString(50, offset - 10, "Skill gaps and suggestions:")
    offset -= 30
    for gap in record.skill_gaps[:3]:
        buffer.drawString(60, offset, f"{gap['area']} gap: {gap['gap']} points")
        offset -= 18
        if gap.get("resources"):
            buffer.drawString(70, offset, f"Resource: {gap['resources'][0]['title']}")
            offset -= 18
    buffer.save()
    return response


def api_predict(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)
    try:
        payload = json.loads(request.body.decode("utf-8"))
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    predictions = predict_placement(payload)
    timeline = predict_timeline(payload)
    companies = get_company_matches(payload)
    return JsonResponse({"prediction": predictions, "timeline": timeline, "company_matches": companies})


def api_github(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)
    try:
        data = json.loads(request.body.decode("utf-8"))
        username = data.get("username", "")
    except Exception:
        username = ""
    return JsonResponse(analyze_github_profile(username))


def api_resume(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)
    result = score_resume(request.FILES.get("resume_file"))
    return JsonResponse(result)


def api_companies(request):
    return JsonResponse({"companies": COMPANIES})


def api_skill_gap(request, pk):
    record = get_object_or_404(StudentRecord, pk=pk)
    student_features = {
        "cgpa": record.cgpa,
        "coding_score": record.coding_score,
        "aptitude_score": record.aptitude_score,
        "communication_score": record.communication_score,
        "projects": record.projects,
        "internships": record.internships,
        "certifications": record.certifications,
        "github_contributions": record.github_contributions,
        "leetcode_solved": record.leetcode_solved,
        "hackathon": record.hackathon,
        "soft_skills": record.soft_skills,
    }
    result = analyze_skill_gap(student_features, record.id)
    return JsonResponse(result)


@csrf_exempt
def api_verify_hackerrank(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            if username:
                result = verify_hackerrank(username)
                return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'verified': False, 'error': str(e)})
    return JsonResponse({'verified': False, 'error': 'Invalid request'})


@csrf_exempt
def api_verify_leetcode(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            if username:
                result = verify_leetcode(username)
                return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'verified': False, 'error': str(e)})
    return JsonResponse({'verified': False, 'error': 'Invalid request'})


# ============ MOCK TEST FUNCTIONS ============

@login_required
def mock_test_list(request):
    """Show all available mock tests"""
    aptitude_tests = MockTest.objects.filter(category='aptitude')
    coding_tests = MockTest.objects.filter(category='coding')
    verbal_tests = MockTest.objects.filter(category='verbal')
    
    # Get user's completed tests
    completed_tests = MockTestResult.objects.filter(user=request.user).values_list('mock_test_id', flat=True)
    
    return render(request, "placement_app/mock_test_list.html", {
        "aptitude_tests": aptitude_tests,
        "coding_tests": coding_tests,
        "verbal_tests": verbal_tests,
        "completed_tests": completed_tests,
    })


@login_required
def mock_test_detail(request, pk):
    """Show a specific mock test with questions"""
    mock_test = get_object_or_404(MockTest, pk=pk)
    
    # Check if user already completed this test
    existing_result = MockTestResult.objects.filter(user=request.user, mock_test=mock_test).first()
    if existing_result:
        messages.warning(request, f"You have already completed this test. Score: {existing_result.percentage}%")
        return redirect('mock_test_results')
    
    questions = mock_test.questions.all()
    
    return render(request, "placement_app/mock_test_detail.html", {
        "mock_test": mock_test,
        "questions": questions,
    })


@login_required
def mock_test_submit(request, pk):
    """Submit mock test answers and calculate score"""
    mock_test = get_object_or_404(MockTest, pk=pk)
    
    if request.method != "POST":
        return redirect('mock_test_detail', pk=pk)
    
    questions = mock_test.questions.all()
    score = 0
    total_marks = 0
    user_answers = {}
    
    for question in questions:
        total_marks += question.marks
        user_answer = request.POST.get(f'question_{question.id}')
        user_answers[str(question.id)] = user_answer
        
        if user_answer and user_answer.upper() == question.correct_answer:
            score += question.marks
    
    percentage = (score / total_marks) * 100 if total_marks > 0 else 0
    
    # Save result
    result = MockTestResult.objects.create(
        user=request.user,
        mock_test=mock_test,
        score=score,
        total_marks=total_marks,
        percentage=round(percentage, 2),
        answers=user_answers,
        completed_at=datetime.now()
    )
    
    # Pass data to celebration results page
    return render(request, "placement_app/mock_test_result_page.html", {
        "result": result,
        "mock_test": mock_test,
        "score": score,
        "total_marks": total_marks,
        "percentage": round(percentage, 2),
        "passed": percentage >= mock_test.passing_score,
        "passing_score": mock_test.passing_score,
    })


@login_required
def mock_test_results(request):
    """Show user's mock test results"""
    results = MockTestResult.objects.filter(user=request.user).order_by('-completed_at')
    
    # Calculate average score
    avg_score = 0
    if results:
        avg_score = sum(r.percentage for r in results) / len(results)
    
    return render(request, "placement_app/mock_test_results.html", {
        "results": results,
        "avg_score": round(avg_score, 2),
    })


# ============ LEADERBOARD FUNCTION ============

@login_required
def leaderboard(request):
    """Show leaderboard of top students based on mock test scores"""
    from django.contrib.auth.models import User
    from django.db.models import Avg, Count
    
    # Get all students who have taken tests
    students = User.objects.filter(test_results__isnull=False).distinct()
    
    leaderboard_data = []
    for student in students:
        results = MockTestResult.objects.filter(user=student)
        avg_score = results.aggregate(Avg('percentage'))['percentage__avg'] or 0
        test_count = results.count()
        
        # Count passed tests
        passed_count = results.filter(percentage__gte=50).count()
        
        # Get latest test score
        latest = results.order_by('-completed_at').first()
        
        leaderboard_data.append({
            'user': student,
            'username': student.username,
            'avg_score': round(avg_score, 2),
            'test_count': test_count,
            'passed_count': passed_count,
            'latest_score': latest.percentage if latest else 0,
            'latest_test': latest.mock_test.title if latest else 'N/A',
            'completed_at': latest.completed_at if latest else None,
        })
    
    # Sort by average score (highest first)
    leaderboard_data.sort(key=lambda x: x['avg_score'], reverse=True)
    
    # Add rank
    for i, item in enumerate(leaderboard_data):
        item['rank'] = i + 1
    
    # Get top 3 for medal display
    top_3 = leaderboard_data[:3] if leaderboard_data else []
    
    return render(request, "placement_app/leaderboard.html", {
        "leaderboard_data": leaderboard_data,
        "top_3": top_3,
        "total_students": len(leaderboard_data),
    })