<template>
  <link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/darkly/bootstrap.min.css"
    integrity="sha384-nNK9n28pDUDDgIiIqZ/MiyO3F4/9vsMtReZK39klb/MtkZI3/LtjSjlmyVPS3KdN"
    crossorigin="anonymous"
  />
  <HomePage />
  <Dashboard v-if="false" />
</template>

<script>
import Dashboard from './components/Dashboard.vue';
import HomePage from './components/HomePage.vue';

export default {
  name: 'App',
  components: {
    Dashboard,
    HomePage,
  },
};
</script>
