<template>
  <div class="nav-bar">
    <el-menu default-active="//course/:cid/semester/:sid/home" mode="horizontal" router>
      <el-menu-item index="/course/:cid/semester/:sid/home">课程名</el-menu-item>
      <el-menu-item index="/course/:cid/semester/:sid/course-calendar">课程日历</el-menu-item>
      <el-menu-item index="/course/:cid/semester/:sid/course-res">课程资源</el-menu-item>
      <el-menu-item :index="$router.path"><el-link href="https://www.ele.me" target="_blank" :underline="false">答疑平台</el-link></el-menu-item>
      <el-submenu index="older">
        <template slot="title">过往学期</template>
        <el-menu-item :index="$router.path">
          <el-link href="https://www.ele.me" target="_blank" type="info" :underline="false" style="display:block;text-align:center;">过往学期1</el-link>
        </el-menu-item>
        <el-menu-item :index="$router.path">
          <el-link href="https://www.ele.me" target="_blank" type="info" :underline="false" style="display:block;text-align:center;">过往学期2</el-link>
        </el-menu-item>
        <el-menu-item :index="$router.path">
          <el-link href="https://www.ele.me" target="_blank" type="info" :underline="false" style="display:block;text-align:center;">过往学期3</el-link>
        </el-menu-item>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped>
.el-menu {
  display: flex;
  justify-content: flex-end;
}

.el-submenu {
  padding-right: 2em;
}

.el-submenu .el-menu-item{
  display: flex;
  justify-content: center;
}

</style>
