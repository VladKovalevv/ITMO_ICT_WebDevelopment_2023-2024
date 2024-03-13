<template>
  <div class="container">
    <div class="consignments-list">
      <h1>Партии товаров</h1>

      <label>Сортировать по:</label>
      <select v-model="sortBy" @change="sortConsignments">
        <option value="date_sold">Дата Продажи</option>
        <option value="cost">Стоимость</option>
      </select>

      <label>Поиск:</label>
      <input class="input" v-model="searchTerm" @input="filterConsignments" />

      <ul>
        <li v-for="consignment in filteredConsignments" :key="consignment.id">
          Дата Продажи: {{ consignment.date_sold }} - Стоимость: {{ consignment.cost }}}
        </li>
      </ul>
    </div>

    <div class="add-consignment-form">
      <h2>Добавить Новую Партию</h2>
      <form @submit.prevent="addConsignment">
        <label for="dateSold">Дата Продажи:</label>
        <input type="date" v-model="newConsignment.date_sold" required />

        <label for="num">Номер:</label>
        <input type="text" v-model="newConsignment.num" required />

        <label for="cost">Стоимость:</label>
        <input type="number" v-model="newConsignment.cost" required />

        <label for="prepayment">Предоплата:</label>
        <input type="checkbox" v-model="newConsignment.prepayment" />

        <label for="broker">ID Брокера:</label>
        <input type="number" v-model="newConsignment.broker" required />

        <button type="submit">Добавить Партию</button>
      </form>
    </div>
  </div>
</template>

  <script>
  import axios from 'axios';

  export default {
    name: 'Consignments',
    data() {
      return {
        consignments: [],
        sortBy: 'date_sold',
        searchTerm: '',
        newConsignment: {
          date_sold: '',
          num: '',
          cost: 0,
          prepayment: false,
          broker: 0,
        },
      };
    },
    computed: {
      sortedConsignments() {
        return this.consignments.slice().sort((a, b) => {
          if (this.sortBy === 'date_sold') {
            return new Date(b.date_sold) - new Date(a.date_sold);
          } else if (this.sortBy === 'cost') {
            return b.cost - a.cost;
          }
          return 0;
        });
      },
      filteredConsignments() {
        const search = this.searchTerm.toLowerCase();
        return this.sortedConsignments.filter(
          consignment => consignment.date_sold.toLowerCase().includes(search)
        );
      },
    },
    methods: {
      async fetchConsignments() {
        try {
          const response = await axios.get('http://127.0.0.1:8000/main/consignments/', {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          this.consignments = response.data;
        } catch (error) {
          console.error('Error fetching consignment data:', error);
        }
      },
      sortConsignments() {
      },
      filterConsignments() {
      },
      async addConsignment() {
        try {
          const response = await axios.post('http://127.0.0.1:8000/main/consignments/', this.newConsignment, {
            headers: {
              Authorization: `Token ${localStorage.getItem('access_token')}`,
            },
          });
          console.log('Consignment added successfully:', response.data);
        } catch (error) {
          console.error('Error adding consignment:', error.response.data);
        }
      },
    },
    created() {
      this.fetchConsignments();
    },
  };
  </script>

<style scoped>
.container {
  display: flex;
  justify-content: space-between;
}

.consignments-list, .add-consignment-form {
  width: 48%; /* Разделение пространства между списком и формой */
  padding: 20px;
}

h1, h2 {
  color: #2c3e50;
}

label {
  display: block;
  margin: 10px 0 5px;
}

select, input[type="text"], input[type="date"], input[type="number"] {
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
input{
  margin-bottom: 10px;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
li {
  padding: 8px;
  margin-bottom: 10px;
  background-color: #f9f9f9;
  border-left: 5px solid #4CAF50;
}
</style>
