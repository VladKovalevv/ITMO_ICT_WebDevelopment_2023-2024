<template>
  <div class="container">
    <nav class="sidebar">
      <router-link v-if="!isAuthPage()" to="/brokers" class="nav-link" :class="{ 'active': $route.path === '/brokers' }">Брокеры</router-link>
      <router-link v-if="!isAuthPage()" to="/producers" class="nav-link" :class="{ 'active': $route.path === '/producers' }">Производители</router-link>
      <router-link v-if="!isAuthPage()" to="/products" class="nav-link" :class="{ 'active': $route.path === '/products' }">Продукты</router-link>
      <router-link v-if="!isAuthPage()" to="/cosignments" class="nav-link" :class="{ 'active': $route.path === '/consignments' }">Партии товаров</router-link>
      <router-link v-if="!isAuthenticated" to="/login" class="nav-link" :class="{ 'active': $route.path === '/login' }">Вход</router-link>
      <router-link v-if="!isAuthenticated" to="/register" class="nav-link" :class="{ 'active': $route.path === '/register' }">Регистрация</router-link>
      <router-link v-if="isAuthenticated" to="/profile" class="nav-link" :class="{ 'active': $route.path === '/profile' }">Профиль</router-link>
      <button v-if="isAuthenticated" @click="logout" class="nav-link logout-button">Выход</button>
    </nav>
  </div>
</template>


  
  <script>
  export default {
    name: 'Navbar',
    data() {
      return {
        isAuthenticated: false,
      };
    },
    methods: {
      isAuthPage() {
        const authPages = ['/login', '/register'];
        return authPages.includes(this.$route.path);
      },
      logout() {
        // Clear authentication token from local storage
        localStorage.removeItem('access_token');
  
        // Update the isAuthenticated status
        this.isAuthenticated = false;
  
        // Redirect to the login page
        this.$router.push('/login');
      },
    },
    created() {
      // Check if the user is already authenticated
      this.isAuthenticated = localStorage.getItem('access_token') !== null;
    },
  };
  </script>
  
  <style scoped>
.container {
  display: flex;
}

.sidebar {
  background-color: #000000;
  color: #ffffff;
  padding: 20px;
  height: 100vh;
  width: 250px; /* Можно настроить по вашему усмотрению */
  flex-shrink: 0; /* Это предотвратит сжатие боковой панели */
}

.nav-link {
  text-decoration: none;
  color: #ffffff;
  font-size: 1.2em;
  display: block; /* Сделаем ссылки блочными элементами */
  padding: 10px;
  border-radius: 4px;
  margin-bottom: 5px; /* Добавим немного места между ссылками */
  transition: color 0.3s;
}

.nav-link:hover,
.active {
  text-decoration: underline;
  color: #9c9c9c;
}

.logout-button {
  background-color: #4d4d4d;
  color: #767676;
  padding: 10px;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
  border-radius: 4px;
  margin-top: 10px;
  transition: color 0.3s;
}

.logout-button:hover {
  color: #f8fa87;
  text-decoration: underline;
}

.content {
  flex-grow: 1; /* Это позволит контенту занимать все доступное пространство */
  padding: 20px;
}
</style>

  