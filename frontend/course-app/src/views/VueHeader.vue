<template>
  <el-row>
    <el-col :span="4">
      <div class="logo">Logo</div>
    </el-col>
    <el-col :span="20">
      <nav-bar></nav-bar>
    </el-col>
  </el-row>
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

<style scoped>
.logo {
  line-height: 60px;
  height: 60px;
  text-align: center;
  border-bottom: solid 1px #e6e6e6;
}
</style>
