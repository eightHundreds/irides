import babelpolyfill from "babel-polyfill";
import Vue from "vue";
import App from "./App";
import 'element-ui/lib/theme-chalk/index.css'
import ElementUI from 'element-ui'
import VueRouter from "vue-router";
//import store from "./vuex/store";
//import Vuex from "vuex";
//import routes from './routes'
//import Mock from './mock'
//Mock.bootstrap();
import axios from "axios";

Vue.use(VueRouter);
Vue.use(ElementUI);

const router = new VueRouter({
  // routes
});

new Vue({
  el: '#app',
  router,
  //store,
  //components: { App }
  render: h => h(App)
});
