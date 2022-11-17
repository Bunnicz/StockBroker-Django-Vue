<template>
  <div class="container">
    <AppHeader title="World Stock Info" />
    <NavbarObj />
    <div class="alert alert-info" v-if="isBusy">Loading...</div>
    <div class="alert alert-danger" v-if="error">{{ error }}</div>
    <router-view></router-view>
    <AppFooter />
  </div>
</template>

<script>
// import axios from 'axios';

import AppHeader from './components/AppHeader';
import AppFooter from './components/AppFooter';
import NavbarObj from './components/NavbarObj';
import store from "./store";
import { computed } from "vue";



export default {
  name: 'App',
  components: {
    AppHeader,
    NavbarObj,
    AppFooter,
  },
  setup() {
    return {
      isBusy: computed(() => store.state.isBusy),
      error: computed(() => store.state.error),
      isAuthenticated: computed(() => store.getters.isAuthenticated),
      onLogout: () => store.dispatch("logout")
    }
  }
}
</script>


<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400&display=swap');

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: 'Poppins', sans-serif;
}

.container {
  max-width: 500px;
  margin: 30px auto;
  overflow: auto;
  min-height: 300px;
  border: 1px solid steelblue;
  padding: 30px;
  border-radius: 5px;
}

.btn {
  display: inline-block;
  background: #000;
  color: #fff;
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 15px;
  font-family: inherit;
}

.btn:focus {
  outline: none;
}

.btn:active {
  transform: scale(0.98);
}

.btn-block {
  display: block;
  width: 100%;
}
.alert {
  position:relative;
  text-align: center;
  margin: 15px auto;
  background: #1f1f1f;
  color: #ff0000;
  overflow: auto;
  border: 2px solid #b44646;
  padding: 30px;
  border-radius: 5px;
}
</style>
