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

4. Start creating a project
    ```bash
    django-admin startproject lab_management       
    cd lab_management
    ```

5. Create an app named labs
    ```bash
    python manage.py startapp labs
    ```

6. Start the server
    ```bash
    python manage.py runserver
    ```

### lab-management-frontend
1. Set up Vue 3 using Vite
    ```bash
    npm create vite@latest lab-management-frontend --template vue
    cd lab-management-frontend
    npm install
    ```

2. Install Axios for API calls
    ```bash
    npm install axios
    ```

3. Configure Tailwind by creating a tailwind.config.js file
    ```bash
    npx tailwindcss init
    ```

4. Run the frontend
    ```bash
    npm run dev
    ```
