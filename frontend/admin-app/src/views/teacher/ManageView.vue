<template>
  <div>
    <el-container>
      <side-bar></side-bar>
      <router-view></router-view>
    </el-container>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
  name: 'ManageView',
  components: {
    SideBar,
  },
};
</script>

<style>

</style>
