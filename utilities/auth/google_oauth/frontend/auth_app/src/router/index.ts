import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterUser from '../components/RegisterUser.vue'
import GoogleRedirect from '../components/GoogleRedirect.vue'
import HomeDashboard from '../views/HomeDashboard.vue';


const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: HomeDashboard
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterUser
  },
  {
    path: '/google-redirect', // Add a route for the Google redirect
    name: 'google-redirect',
    component: GoogleRedirect,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
