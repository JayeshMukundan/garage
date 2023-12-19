<template>
  <div>
    <h2>Google OAuth Redirect</h2>
    <p>Redirecting...</p>
  </div>
</template>

<script lang="ts">
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';
import Cookies from 'js-cookie';
import router from '../router'


export default {
  setup() {
    const route = useRoute();

    onMounted(() => {
      // Extract access token from URL parameters
      const params = new URLSearchParams(route.fullPath.split('?')[1]);
      const accessToken  = params.get('access_token') || '';
      Cookies.set('access_token', accessToken, { httpOnly: true });
      localStorage.setItem('accessToken', accessToken);
    });
    router.push({ name: 'dashboard' });
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
