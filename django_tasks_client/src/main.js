import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import router from './router/index'

import ApiPlugin from './plugins/api'
import LoadPlugin from './plugins/load'

import axios from 'axios'
import {BootstrapVue} from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/js/bootstrap.bundle';

Vue.config.productionTip = false
Vue.prototype.$http = axios;
Vue.use(VueRouter)
Vue.use(ApiPlugin)
Vue.use(LoadPlugin)
Vue.use(BootstrapVue)

new Vue({
  render: h => h(App),
  router,
  axios,

}).$mount('#app')
