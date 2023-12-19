import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

// Import the Register component
import RegisterUser from './components/RegisterUser.vue'

// Create the Vue app instance
const app = createApp(App)

// Register the Register component globally
app.component('RegisterUser', RegisterUser)

// Use Vue Router
app.use(router)

// Mount the app
app.mount('#app')

//createApp(App).use(router).mount('#app')
