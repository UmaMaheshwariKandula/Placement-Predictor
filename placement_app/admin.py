from django.contrib import admin
from .models import Profile, StudentRecord, MockTest, MockTestQuestion, MockTestResult

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role")
    list_filter = ("role",)
    search_fields = ("user__username",)

@admin.register(StudentRecord)
class StudentRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "cgpa", "placement_probability", "placement_month", "created_at")
    list_filter = ("placement_month",)
    search_fields = ("user__username",)

# ============ MOCK TEST ADMIN ============

@admin.register(MockTest)
class MockTestAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "time_limit", "passing_score", "created_at")
    list_filter = ("category", "created_at")
    search_fields = ("title",)
    ordering = ("-created_at",)

@admin.register(MockTestQuestion)
class MockTestQuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "mock_test", "question_text", "correct_answer", "marks")
    list_filter = ("mock_test",)
    search_fields = ("question_text",)

@admin.register(MockTestResult)
class MockTestResultAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "mock_test", "score", "total_marks", "percentage", "completed_at")
    list_filter = ("mock_test", "completed_at")
    search_fields = ("user__username",)
    actions = ["delete_selected_results"]
    
    def delete_selected_results(self, request, queryset):
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f'Successfully deleted {count} test result(s).')
    delete_selected_results.short_description = "Delete selected test results"