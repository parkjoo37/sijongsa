import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import router from "./router";
import store from './store';
// import axios from 'axios';
// import VueRouter from 'vue-router'
// import { MainPage, LoginPage, SignUpPage } from './components'

// Vue.prototype.$axios = axios;
Vue.config.productionTip = false

// Vue.use(VueRouter)

// const routes = [
//   {
//     path: '/',
//     component: MainPage
//   },
//   {
//     path: '/login',
//     component: LoginPage
//   },
//   {
//     path: '/signup',
//     component: SignUpPage
//   }
// ];

// const router = new VueRouter({
//     mode: 'history',
//     routes
// });

new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
