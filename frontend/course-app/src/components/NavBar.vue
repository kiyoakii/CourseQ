<template>
  <div class="nav-bar">
    <el-menu mode="horizontal" router>
      <el-menu-item :index="'/course/' + $route.params.cid + '/home'">课程主页</el-menu-item>
      <!-- <el-menu-item :index="'/course/' + $route.params.cid + '/calendar'">课程日历</el-menu-item>
      <el-menu-item :index="'/course/' + $route.params.cid + '/resourse'">课程资源</el-menu-item> -->
      <el-menu-item :index="$router.path">
        <el-link :index="'/proans/course/' + $route.params.cid" target="_blank" :underline="false">
          答疑平台
        </el-link>
      </el-menu-item>
      <el-submenu index="older" router>
        <template slot="title">过往学期</template>
        <div v-for="(course, i) in allinfo.series_courses" :key="i">
          <el-menu-item :index="$router.path">
            <el-link :href="'/#/course/' + course.cid + '/home'" :underline="false"
              style="display:block;text-align:center;">
              {{ course.name_zh + course.semester }}
            </el-link>
          </el-menu-item>
        </div>
      </el-submenu>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    allinfo: {},
  },
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
