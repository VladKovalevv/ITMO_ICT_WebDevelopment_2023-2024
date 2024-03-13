<template>
  <div class="container">
    <div class="products-list">
      <h1>Продукты</h1>

      <label>Сортировать по:</label>
      <select v-model="sortBy" @change="sortProducts">
        <option value="code">Код</option>
        <option value="name">Название</option>
        <option value="unit">Единица измерения</option>
        <option value="shelf_life">Срок хранения</option>
      </select>

      <label>Поиск по коду:</label>
      <input class="input" v-model="searchTerm" @input="filterProducts" />

      <ul>
        <li v-for="product in filteredProducts" :key="product.id">
          {{ product.code }} - {{ product.name }} - {{ product.unit }} - {{ product.shelf_life }}
        </li>
      </ul>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'Products',
    data() {
      return {
        products: [],
        sortBy: 'code',
        searchTerm: '',
      };
    },
    computed: {
      sortedProducts() {
        return this.products.slice().sort((a, b) => {
          if (this.sortBy === 'code') {
            return a.code.localeCompare(b.code);
          } else if (this.sortBy === 'name') {
            return a.name.localeCompare(b.name);
          } else if (this.sortBy === 'unit') {
            return a.unit.localeCompare(b.unit);
          } else if (this.sortBy === 'shelf_life') {
            return a.shelf_life - b.shelf_life;
          }
          return 0;
        });
      },
      filteredProducts() {
        const search = this.searchTerm.toLowerCase();
        return this.sortedProducts.filter(
          product => product.code.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchProducts() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/products/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.products = response.data;
        } catch (error) {
          console.error('Error fetching product data:', error);
        }
      },
      sortProducts() {
        // Triggered when sorting option changes
      },
      filterProducts() {
        // Triggered when search term changes
      },
    },
    created() {
      this.fetchProducts();
    },
  };
  </script>
  
 <style scoped>
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.products-list {
  width: 100%;
}

h1 {
  color: #2c3e50;
}

label {
  display: block;
  margin: 10px 0 5px;
}

select, .input {
  width: 100%;
  padding: 8px;
  margin: 5px 0 20px;
  border-radius: 4px;
  border: 1px solid #ccc;
}

button {
  background-color: #000000;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #45a049;
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
  