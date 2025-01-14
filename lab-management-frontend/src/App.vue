<script setup>
import axios from 'axios';
import AddLabForm from './components/AddLabForm.vue';
import LabList from './components/LabList.vue';
</script>

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
