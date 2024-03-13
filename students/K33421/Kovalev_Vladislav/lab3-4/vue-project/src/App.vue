<template>
  <div id="app" class="app-container">
    <Navbar class="app-navbar" />
    <div class="app-content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue';

export default {
  name: 'App',
  components: {
    Navbar,
  },
};
</script>

<style>
#app {
  display: flex;
  min-height: 100vh;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #2c3e50;
}

.app-container {
  display: flex;
  flex-direction: row;
}

.app-navbar {
  min-width: 250px;
  max-width: 250px;
}

.app-content {
  flex-grow: 1;
  text-align: left;
  padding: 20px;
}
</style>
