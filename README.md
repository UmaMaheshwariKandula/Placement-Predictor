# Placement Success AI System

**Live Demo:** [Click here to view the live website] (https://umamaheshwari.pythonanywhere.com)

A complete local placement success prediction system built with Django, Django REST Framework, and scikit-learn. The system includes student/faculty/officer dashboards, GitHub profile analysis, resume scoring, company matching, skill gap learning paths, report generation, and synthetic ML training.

## Setup

1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python data_generator.py
5. python train.py
6. python manage.py migrate
7. python manage.py createsuperuser (optional)
8. python manage.py runserver

## Features

- Role-based authentication: Student, Faculty, Placement Officer
- Predict placement probability with Logistic Regression, Random Forest, XGBoost
- GitHub Analyzer and Resume Scorer
- Company Matcher and Placement Timeline
- What-if simulator, Skill-gap analysis, Early warning system
- Peer comparison, PDF report generation, mock job demand insights

## API Endpoints

- POST /api/predict/
- POST /api/github/
- POST /api/resume/
- GET /api/companies/
- GET /api/skill-gap/<id>/
