import { createRouter, createWebHistory } from 'vue-router';
import SignUp from '../components/SignUp.vue';
import UserDashboard from '../components/UserDashboard.vue';

const routes = [
  {
    path: '/',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/dashboard',
    name: 'UserDashboard',
    component: UserDashboard
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
