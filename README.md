Django Project Setup Guide
==========================

This project is built with Django. Follow the steps below to run it locally on your machine.

Requirements
------------
- Python 3.8 or above
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git (to clone the project)

Setup Instructions
------------------

1. Clone the project:
   git clone https://github.com/vikeshkumar8210/demo_project.git
   cd your-project-name

2. Create a virtual environment (recommended):
   python -m venv env
   source env/bin/activate         # On Windows: env\\Scripts\\activate

3. Install required packages:
   pip install -r requirements.txt

   If requirements.txt is missing, install Django manually:
   pip install django

4. Apply database migrations:
   python manage.py migrate

5. Create a superuser (admin account):
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver

7. Open your browser and go to:
   - Home: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/
  
### 🔐 Login Page Screenshot

![Login Page](https://github.com/vikeshkumar8210/demo_project/blob/main/login.png)

### Admin Page Screenshot
![Admin page](https://github.com/vikeshkumar8210/demo_project/blob/main/admin.png)

Notes
-----
- Default database: SQLite (no setup needed)
- Always activate your virtual environment before running the project.

