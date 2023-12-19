<!-- HomeDashboard.vue -->

<template>
  <div>
    <h2>Welcome to the Home Dashboard</h2>

    <!-- Your dashboard content goes here -->

    <a @click="callSayHelloAPI" href="#">Call /api/say_hello</a>
    <!-- Display the API response -->
    <p v-if="apiResponse">{{ apiResponse }}</p>
    <br/>
    <a @click="logoutAPI" href="#">Call /api/logout</a>
    <p v-if="logoutApiResponse">{{ logoutApiResponse }}</p>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  setup() {
    // Your existing setup logic
    const apiResponse = ref('');
    const logoutApiResponse = ref('');

    const callSayHelloAPI = async () => {
      
      try {
        // Make a request to the backend API with the access token
        const response = await axios.get('/api/say_hello', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          },
        });

        // Handle the response as needed
        apiResponse.value = response.data;
      } catch (error) {
        console.error('Error during API call:', error);
        apiResponse.value = 'Error during API call';
      }
    };
    const logoutAPI = async () => {
      
      try {
        // Make a request to the backend API with the access token
        const response = await axios.get('/api/logout', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
          },
        });

        // Handle the response as needed
        logoutApiResponse.value = response.data;
      } catch (error) {
        console.error('Error during API call:', error);
        logoutApiResponse.value = 'Error during API call';
      }
    };

    return { callSayHelloAPI, apiResponse, logoutAPI, logoutApiResponse, /* other variables */ };
  },
};
</script>
