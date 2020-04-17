<template>
  <div class="vue-header">
    <p>This is VueHeader component.</p>
    <nav-bar></nav-bar>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'VueHeader',
  components: {
    NavBar,
  },
};
</script>

<style>

</style>
