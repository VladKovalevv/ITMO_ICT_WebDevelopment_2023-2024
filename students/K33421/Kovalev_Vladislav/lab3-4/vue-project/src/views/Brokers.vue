<template>
  <div class="container">
    <h1>Брокеры</h1>

    <!-- Опции сортировки -->
    <label>Сортировать по:</label>
    <select v-model="sortBy" @change="sortBrokers">
      <option value="name">Имя</option>
      <option value="income">Доход</option>
    </select>

    <!-- Поиск -->
    <label>Поиск:</label>
    <input class="input" v-model="searchTerm" @input="filterBrokers" />

    <!-- Список брокеров -->
    <ul>
      <li v-for="broker in filteredBrokers" :key="broker.id">
        {{ broker.name }} - Доход: {{ broker.income }} - ID {{broker.id}}
      </li>
    </ul>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Brokers',
    data() {
      return {
        brokers: [],
        sortBy: 'name',
        searchTerm: '',
      };
    },
    computed: {
      sortedBrokers() {
        return this.brokers.slice().sort((a, b) => {
          if (this.sortBy === 'name') {
            return a.name.localeCompare(b.name);
          } else if (this.sortBy === 'income') {
            return b.income - a.income;
          }
          return 0;
        });
      },
      filteredBrokers() {
        const search = this.searchTerm.toLowerCase();
        return this.sortedBrokers.filter(
          broker => broker.name.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchBrokers() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/brokers/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.brokers = response.data;
        } catch (error) {
          console.error('Error fetching broker data:', error);
        }
      },
      sortBrokers() {
        // Triggered when sorting option changes
      },
      filterBrokers() {
        // Triggered when search term changes
      },
    },
    created() {
      this.fetchBrokers();
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

.select, .input {
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
  