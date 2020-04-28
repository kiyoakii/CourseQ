<template>
  <div>
    <el-container>
      <router-view name="sidebar"></router-view>
      <router-view name="content"></router-view>
    </el-container>
  </div>
</template>

<script>
export default {
  name: 'VueContent',
};
</script>

<style>

</style>
