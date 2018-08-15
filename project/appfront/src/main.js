// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import store from "../node_modules/store/dist/store.legacy.min";
import '../theme/index.css'
import VueResource from 'vue-resource'
import 'normalize.css'
import axios from 'axios';
Vue.config.productionTip = false

Vue.use(store);
Vue.use(ElementUI);
Vue.use(VueResource) 
Vue.prototype.$ajax = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  components: { App },
  template: '<App/>'
})
