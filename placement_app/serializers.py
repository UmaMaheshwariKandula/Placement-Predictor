from rest_framework import serializers
from .models import StudentRecord

class StudentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRecord
        fields = [
            "id",
            "user",
            "cgpa",
            "backlogs",
            "coding_score",
            "aptitude_score",
            "communication_score",
            "projects",
            "internships",
            "certifications",
            "github_contributions",
            "leetcode_solved",
            "hackathon",
            "soft_skills",
            "resume_score",
            "github_score",
            "placement_probability",
            "placement_month",
            "company_matches",
            "skill_gaps",
            "created_at",
        ]
