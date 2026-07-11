from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    ROLE_CHOICES = [
        ("student", "Student"),
        ("faculty", "Faculty"),
        ("officer", "Placement Officer"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"


class StudentRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="records")
    
    # Academic features
    cgpa = models.FloatField(default=0.0)
    backlogs = models.IntegerField(default=0)
    
    # Skill scores
    coding_score = models.IntegerField(default=0)
    aptitude_score = models.IntegerField(default=0)
    communication_score = models.IntegerField(default=0)
    soft_skills = models.IntegerField(default=0)
    
    # Experience
    projects = models.IntegerField(default=0)
    internships = models.IntegerField(default=0)
    certifications = models.IntegerField(default=0)
    
    # Technical achievements
    github_contributions = models.IntegerField(default=0)
    leetcode_solved = models.IntegerField(default=0)
    hackathon = models.IntegerField(default=0)
    
    # Scores from external tools
    resume_score = models.IntegerField(default=0)
    github_score = models.IntegerField(default=0)
    
    # Predictions
    placement_probability = models.FloatField(default=0.0)
    placement_month = models.IntegerField(default=12)
    company_matches = models.JSONField(default=list, blank=True)
    skill_gaps = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ============ VERIFICATION PROOF FIELDS ============
    
    # Academic proofs
    cgpa_proof = models.FileField(upload_to='proofs/cgpa/', null=True, blank=True)
    backlog_proof = models.FileField(upload_to='proofs/backlogs/', null=True, blank=True)
    
    # Coding verification
    coding_proof_url = models.URLField(max_length=500, null=True, blank=True)
    coding_platform = models.CharField(max_length=50, null=True, blank=True)
    coding_username = models.CharField(max_length=100, null=True, blank=True)
    
    # Aptitude verification
    aptitude_exam_name = models.CharField(max_length=100, null=True, blank=True)
    aptitude_proof = models.FileField(upload_to='proofs/aptitude/', null=True, blank=True)
    
    # Communication verification
    communication_certificate = models.FileField(upload_to='proofs/communication/', null=True, blank=True)
    
    # Projects verification
    project_repo_links = models.TextField(null=True, blank=True)
    
    # Internship verification
    internship_certificate = models.FileField(upload_to='proofs/internship/', null=True, blank=True)
    
    # Certification verification
    certification_links = models.TextField(null=True, blank=True)
    
    # Coding platform usernames
    github_username = models.CharField(max_length=100, null=True, blank=True)
    leetcode_username = models.CharField(max_length=100, null=True, blank=True)
    hackerrank_username = models.CharField(max_length=100, null=True, blank=True)
    
    # Hackathon verification
    hackathon_certificate = models.FileField(upload_to='proofs/hackathon/', null=True, blank=True)
    
    # Soft skills justification
    soft_skills_basis = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Record {self.id} for {self.user.username if self.user else 'Guest'}"


# ============ MOCK TEST MODELS ============

class MockTest(models.Model):
    CATEGORY_CHOICES = [
        ('aptitude', 'Aptitude Test'),
        ('coding', 'Coding Test'),
        ('verbal', 'Verbal Ability'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    time_limit = models.IntegerField(help_text="Time limit in minutes", default=30)
    passing_score = models.IntegerField(default=40)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class MockTestQuestion(models.Model):
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])
    explanation = models.TextField(blank=True, null=True)
    marks = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question_text[:50]


class MockTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
    mock_test = models.ForeignKey(MockTest, on_delete=models.CASCADE)
    score = models.IntegerField()
    total_marks = models.IntegerField()
    percentage = models.FloatField()
    answers = models.JSONField(default=dict)
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.mock_test.title} - {self.percentage}%"