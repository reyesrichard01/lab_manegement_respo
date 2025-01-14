# Lab Management System

## Setup Instructions

### lab_management
1. Create a virtual environment
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment
    ```bash
    .\venv\Scripts\activate
    ```

3. Install Python dependencies:
    ```bash
    pip install django djangorestframework psycopg2
    ```

4. Create an app named labs
    ```bash
    python manage.py startapp labs
    ```

5. Set up PostgreSQL database in settings.py.
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lab_management_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
    ```


