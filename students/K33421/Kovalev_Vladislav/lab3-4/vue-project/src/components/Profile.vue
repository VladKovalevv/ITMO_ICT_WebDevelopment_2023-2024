<template>
  <div class="container">
    <div class="profile-info">
      <h2>Профиль</h2>
      <div class="info-item"><strong>Логин:</strong> {{ userData.username }}</div>
      <div class="info-item"><strong>Email:</strong> {{ userData.email }}</div>
    </div>

    <div class="profile-settings">
      <div class="settings-panel">
        <button @click="toggleSettingsPanel">Change User Data</button>

        <div v-show="showSettingsPanel" class="settings-dropdown">
          <button @click="toggleChangeUsernameForm">Change Username</button>
          <button @click="toggleChangePasswordForm">Change Password</button>
        </div>
      </div>

      <div v-if="showChangePasswordForm" class="change-form">
        <form @submit.prevent="changePassword" class="form">
          <label for="currentPassword">Current Password:</label>
          <input type="password" v-model="currentPassword" required />

          <label for="newPassword">New Password:</label>
          <input type="password" v-model="newPassword" required />

          <button type="submit">Change Password</button>
        </form>
      </div>

      <div v-if="showChangeUsernameForm" class="change-form">
        <form @submit.prevent="changeUsername" class="form">
          <label for="currentPassword">Current Password:</label>
          <input type="password" v-model="currentPassword" required />

          <label for="newUsername">New Username:</label>
          <input type="text" v-model="newUsername" required />

          <button type="submit">Change Username</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      showChangePasswordForm: false,
      showChangeUsernameForm: false,
      showSettingsPanel: false,
      currentPassword: '',
      newPassword: '',
      newUsername: '',
      userData: {},
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    async fetchUserData() {
      console.log('Fetching user data...');

      try {
        const response = await axios.get('/auth/users/me/', {
          headers: {
            'Authorization': `Token ${localStorage.getItem('access_token')}`,
          },
        });
        this.userData = response.data;
        console.log('User data:', this.userData);
      } catch (error) {
        console.error('Error fetching user data:', error.response.data);
      }
    },
    async changePassword() {
      try {
        const response = await axios.post('/auth/users/set_password/', {
          new_password: this.newPassword,
          current_password: this.currentPassword,
        }, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('access_token')}`,
          },
        });

        console.log('Password changed successfully:', response.data);
        this.showChangePasswordForm = false;
      } catch (error) {
        console.error('Password change failed:', error.response.data);
      }
    },
    async changeUsername() {
      try {
        const response = await axios.post('/auth/users/set_username/', {
          current_password: this.currentPassword,
          new_username: this.newUsername,
        }, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('access_token')}`,
          },
        });

        console.log('Username changed successfully:', response.data);
        this.showChangeUsernameForm = false;
      } catch (error) {
        console.error('Username change failed:', error.response.data);
      }
    },
    toggleSettingsPanel() {
      this.showSettingsPanel = !this.showSettingsPanel;
    },
    toggleChangePasswordForm() {
      this.showChangePasswordForm = !this.showChangePasswordForm;
    },
    toggleChangeUsernameForm() {
      this.showChangeUsernameForm = !this.showChangeUsernameForm;
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.1);
  background: #fff;
  max-width: 600px;
  margin: 40px auto;
}

h2 {
  color: #2c3e50;
  margin-bottom: 1em;
}

.profile-info, .profile-settings {
  margin-bottom: 1em;
}

.info-item, .settings-panel, .change-form {
  margin-bottom: 10px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input[type="password"], input[type="text"], select {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  background-color: #4CAF50;
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

.settings-dropdown {
  display: none; /* Initially hide the dropdown */
  flex-direction: column;
  align-items: center;
}

.settings-panel > button {
  margin-bottom: 0.5em; /* Spacing for the toggle button */
}

.settings-dropdown > button {
  margin-bottom: 0.5em;
}

.change-form {
  padding: 15px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.form {
  display: flex;
  flex-direction: column;
}
</style>
