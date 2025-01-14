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
        'USER': 'your_usernam',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
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

4. configure tailwind.config.js
    ```bash
    module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
    ```

5. Add Tailwind directives to src/index.css
    ```bbash
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    ```

6. Build the Vue Components
    ```bash
    LabList.vue
    AddLabForm.vue
    ```

7. App.vue - Combine the components
    ```bash
    <template>
  <div class="min-h-screen bg-gray-100">
    <div class="container mx-auto">
      <h1 class="text-4xl text-center my-6">Lab Management</h1>
      <AddLabForm @lab-added="handleLabAdded" />
      <LabList :labs="labs" />
    </div>
  </div>
</template>

<script>
import AddLabForm from './components/AddLabForm.vue';
import LabList from './components/LabList.vue';

export default {
  components: {
    AddLabForm,
    LabList,
  },
  data() {
    return {
      labs: [],
    };
  },
  methods: {
    handleLabAdded(newLab) {
      this.labs.push(newLab);
    },
  },
  created() {
    this.fetchLabs();
  },
  methods: {
    async fetchLabs() {
      const response = await axios.get('http://localhost:8000/api/labs/');
      this.labs = response.data;
    },
  },
};
</script>
    
    ```

8. Run the frontend
    ```bash
    npm run dev
    ```

-change 1