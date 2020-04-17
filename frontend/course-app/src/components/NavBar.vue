<template>
  <div class="nav-bar">
    <el-menu default-active="/" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="/">课程名</el-menu-item>
      <el-menu-item index="/course-calendar">课程日历</el-menu-item>
      <el-menu-item index="/course-res">课程资源</el-menu-item>
      <el-menu-item :index="$router.path"><a href="https://www.ele.me" target="_blank">答疑平台</a></el-menu-item>
      <el-submenu index="older">
        <template slot="title">过往学期</template>
        <el-menu-item :index="$router.path"><a href="https://www.ele.me" target="_blank">过往学期1</a></el-menu-item>
        <el-menu-item :index="$router.path"><a href="https://www.ele.me" target="_blank">过往学期2</a></el-menu-item>
        <el-menu-item :index="$router.path"><a href="https://www.ele.me" target="_blank">过往学期3</a></el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  methods: {
    handleRoute(key, keypath) {
      console.log(key, keypath, this.$event);
      // this.$router.push('/course-res');
    },
  },
};
</script>

<style scoped>

</style>>
