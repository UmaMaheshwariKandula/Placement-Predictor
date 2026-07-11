@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo Setup complete. Run:
echo python data_generator.py
echo python train.py
echo python manage.py migrate
echo python manage.py runserver
