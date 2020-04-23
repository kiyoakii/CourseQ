<template>
  <div id="app">
    <div class="header">
      <vue-header></vue-header>
    </div>
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
* {
  margin: 0;
  padding: 0;
}


#app {
  font-family: BlinkMacSystemFont, Helvetica Neue, PingFang SC, Microsoft YaHei, Source Han Sans SC,
               Noto Sans CJK SC, WenQuanYi Micro Hei, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
}

</style>
