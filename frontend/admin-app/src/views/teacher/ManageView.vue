<template>
  <div>
    <el-container>
      <side-bar></side-bar>
      <router-view :allInfo="allInfo"></router-view>
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
  computed: {
    allInfo() {
      return this.$store.getters.courseAllInfo(this.$route.params.cid);
    },
  },
};
</script>

<style>

</style>
