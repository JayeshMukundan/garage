<template>
  <div>
    <h2>Register</h2>

    <!-- Password-Based Registration Form -->
    <form v-if="registrationMethod === 'password'" @submit.prevent="registerWithPassword">
      <label for="username">Username:</label>
      <input type="text" v-model="username" required>

      <label for="password">Password:</label>
      <input type="password" v-model="password" required>

      <button type="submit">Register with Password</button>
    </form>

    <!-- Google OAuth Registration Button -->
    <button v-if="registrationMethod === 'google'" @click="registerWithGoogle">
      Register with Google
    </button>

    <!-- Switch Registration Method -->
    <div>
      <label>Registration Method:</label>
      <select v-model="registrationMethod">
        <option value="password">Password</option>
        <option value="google">Google</option>
      </select>
    </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';

export default {
  setup() {
    const username = ref('');
    const password = ref('');
    const registrationMethod = ref('password');

    const registerWithPassword = async () => {
      try {
        console.log('Registered with password');
        // Make an API call to your Flask backend to register with username and password
        // Example: await axios.post('/api/register', { username: username.value, password: password.value });
      } catch (error) {
        console.error('Error during registration:', error);
      }
    };

    const registerWithGoogle = async () => {
      try {
        // Construct the Google Auth URL directly
        const backendUrl = '/api/login/google';        
        // Redirect to the Google Auth URL
        window.location.href = backendUrl;
      } catch (error) {
        console.error('Error:', error);
      }
      console.log('Redirecting to Google OAuth for registration');
    };

    return { username, password, registrationMethod, registerWithPassword, registerWithGoogle };
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
