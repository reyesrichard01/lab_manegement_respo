<template>
  <div class="p-4 bg-gray-100 min-h-screen">
    <h1 class="text-2xl font-semibold mb-4 text-gray-800">Available Labs</h1>
    <ul>
      <li v-for="lab in labs" :key="lab.id" class="mb-4 border p-4 rounded-lg shadow-sm bg-white hover:shadow-md transition-shadow duration-300">
        <h2 class="text-xl font-medium text-gray-700 mb-2">{{ lab.name }}</h2>
        <p class="text-gray-600 mb-2">{{ lab.description }}</p>
        <p class="text-gray-600"><strong>Instructor:</strong> {{ lab.instructor }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      labs: [],
    };
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
