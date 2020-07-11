import Vue from 'vue';
import VueRouter from 'vue-router';
import { MainPage, LoginPage, SignUpPage } from './components';

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: MainPage
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpPage
  }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

export default router;
