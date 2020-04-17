<template>
  <div id="app">
    <vue-header></vue-header>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import VueHeader from './views/VueHeader.vue';

export default {
  name: 'app',
  components: {
    VueHeader,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3b5875;
  margin-top: 60px;
}
</style>
