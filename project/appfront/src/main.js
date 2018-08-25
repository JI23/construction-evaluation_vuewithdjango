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
import qs from 'qs'
Vue.config.productionTip = false

Vue.use(store);
Vue.use(ElementUI);
Vue.use(VueResource) 


//axios.defaults.timeout = 5000;  //设置超时时间
axios.defaults.baseURL = 'http://localhost:8000/api/'; //这是调用数据接口
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8';


axios.interceptors.request.use(
    config => {
        const token = localStorage.getItem("token"); //获取存储在本地的token
        if(token){
            config.headers.Authorization = `token ${store.state.token}`;
            if(config.method === 'post'){
                config.data = qs.stringify(config.data);
            }
        }
        return config;
    },
    err => {
        return Promise.reject(err);
    }
);
Vue.prototype.$ajax = axios


//登陆验证
router.beforeEach((to, from, next) =>{
    if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
        if (store.state.token) {  // 通过vuex state获取当前的token是否存在
            next();
        }
        else {
            next({
                path: '/login',
                query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
            })
        }
    }
    else {
        next();
    }
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  components: { App },
  template: '<App/>'
})
