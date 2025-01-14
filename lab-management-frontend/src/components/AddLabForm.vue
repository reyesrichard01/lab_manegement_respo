<template>
  <div class="p-4 max-w-md mx-auto mt-6 bg-white shadow-lg rounded-lg">
    <h2 class="text-2xl font-semibold mb-4 text-center text-gray-800">Add a New Lab</h2>
    <form @submit.prevent="addLab" class="space-y-4">
      <input v-model="newLab.name" type="text" placeholder="Lab Name" class="input w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
      <input v-model="newLab.description" type="text" placeholder="Description" class="input w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
      <input v-model="newLab.instructor" type="text" placeholder="Instructor" class="input w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500" />
      <button type="submit" class="btn w-full bg-blue-500 text-white p-2 rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500">Add Lab</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      newLab: {
        name: '',
        description: '',
        instructor: '',
      },
    };
  },
  methods: {
    async addLab() {
      const response = await axios.post('http://localhost:8000/api/labs/', this.newLab);
      this.$emit('lab-added', response.data);
      this.newLab.name = '';
      this.newLab.description = '';
      this.newLab.instructor = '';
    },
  },
};
</script>
