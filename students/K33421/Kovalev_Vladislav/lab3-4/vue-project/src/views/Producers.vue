<template>
  <div class="container">
    <h1>Компании-производители</h1>

    <!-- Поиск -->
    <label>Поиск по названию:</label>
    <input class="input" v-model="searchTerm" @input="filterProducers" />

    <!-- Список производителей -->
    <ul>
      <li v-for="producer in filteredProducers" :key="producer.id">
        {{ producer.name }}
      </li>
    </ul>
  </div>
</template>

  <script>
  import axios from 'axios';

  export default {
    name: 'Producers',
    data() {
      return {
        producers: [],
        searchTerm: '',
      };
    },
    computed: {
      filteredProducers() {
        const search = this.searchTerm.toLowerCase();
        return this.producers.filter(
          producer => producer.name.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchProducers() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/companies/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.producers = response.data;
        } catch (error) {
          console.error('Error fetching producer data:', error);
        }
      },
      filterProducers() {
        // Triggered when search term changes
      },
    },
    created() {
      this.fetchProducers();
    },
  };
  </script>

<style scoped>
.container {
  padding: 20px;
}

h1 {
  color: #2c3e50;
}

label {
  display: block;
  margin: 10px 0 5px;
}

.input {
  width: 100%;
  padding: 8px;
  margin: 5px 0 20px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  padding: 8px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  border-left: 5px solid #4CAF50;
}
</style>