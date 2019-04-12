import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
// index.js or main.js
import 'vuetify/dist/vuetify.min.css'


Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
