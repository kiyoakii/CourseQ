<template>
  <div>
    <el-container>
      <el-aside>
        <side-bar></side-bar>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
  name: 'VueContent',
  components: {
    SideBar,
  },
};
</script>

<style>

</style>
