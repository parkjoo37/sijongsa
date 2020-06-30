import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router'
import { MainPage } from './components'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: MainPage
  }
];

const router = new VueRouter({
    mode: 'history',
    routes
});

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
