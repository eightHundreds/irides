import babelpolyfill from "babel-polyfill";
import Vue from "vue";
import App from "./App";
import VueRouter from "vue-router";
//import store from "./vuex/store";
//import Vuex from "vuex";
//import routes from './routes'
//import Mock from './mock'
//Mock.bootstrap();
import axios from "axios";

Vue.use(VueRouter);

const router = new VueRouter({
  // routes
});

new Vue({
  el: '#app',
  //template: '<App/>',
  router,
  //store,
  //components: { App }
  render: h => h(App)
});
