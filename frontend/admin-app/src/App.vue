<template>
  <div id="app">
    <div class="header">
      <vue-hedaer></vue-hedaer>
    </div>
    <div class="content">
      <vue-content></vue-content>
    </div>
  </div>
</template>

<script>
import VueHeader from './views/VueHeader.vue';
import VueContent from './views/VueContent.vue';

export default {
  name: 'app',
  components: {
    VueHeader,
    VueContent,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
