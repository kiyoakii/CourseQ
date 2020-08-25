<template>
  <div>
    <router-view :allinfo="allinfo"></router-view>
  </div>
</template>

<script>
export default {
  name: 'VueContent',
  props: {
    allinfo: {},
  },
};
</script>

<style scoped>

</style>
