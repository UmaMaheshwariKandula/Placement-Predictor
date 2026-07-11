from django.contrib import admin
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ============ ADMIN ============
    path('admin/', admin.site.urls),
    
    # ============ HOME & AUTHENTICATION ============
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # ============ PASSWORD RESET URLS ============
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='placement_app/password_reset.html',
             email_template_name='placement_app/password_reset_email.html',
             subject_template_name='placement_app/password_reset_subject.txt',
             success_url=reverse_lazy('password_reset_done')
         ),
         name='password_reset'),
    
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='placement_app/password_reset_done.html'
         ),
         name='password_reset_done'),
    
    path('password-reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='placement_app/password_reset_confirm.html',
             success_url=reverse_lazy('password_reset_complete')
         ),
         name='password_reset_confirm'),
    
    path('password-reset/complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='placement_app/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    
    # ============ DASHBOARD URLS ============
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('faculty/', views.faculty_dashboard, name='faculty_dashboard'),
    path('officer/', views.officer_dashboard, name='officer_dashboard'),
    path('report/<int:pk>/', views.download_report, name='download_report'),
    
    # ============ API ENDPOINTS ============
    path('api/predict/', views.api_predict, name='api_predict'),
    path('api/github/', views.api_github, name='api_github'),
    path('api/resume/', views.api_resume, name='api_resume'),
    path('api/companies/', views.api_companies, name='api_companies'),
    path('api/skill-gap/<int:pk>/', views.api_skill_gap, name='api_skill_gap'),
    
    # ============ VERIFICATION API ENDPOINTS ============
    path('api/verify-hackerrank/', views.api_verify_hackerrank, name='api_verify_hackerrank'),
    path('api/verify-leetcode/', views.api_verify_leetcode, name='api_verify_leetcode'),
    
    # ============ MOCK TEST URLS ============
    path('mock-tests/', views.mock_test_list, name='mock_test_list'),
    path('mock-test/<int:pk>/', views.mock_test_detail, name='mock_test_detail'),
    path('mock-test/<int:pk>/submit/', views.mock_test_submit, name='mock_test_submit'),
    path('mock-test-results/', views.mock_test_results, name='mock_test_results'),
    
    # ============ LEADERBOARD ============
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]