<template>
  <div class="nav-bar">
    <el-menu mode="horizontal">
      <el-menu-item><a>课程主页</a></el-menu-item>
      <!-- <el-menu-item :index="'/course/' + $route.params.cid + '/calendar'">课程日历</el-menu-item>
      <el-menu-item :index="'/course/' + $route.params.cid + '/resourse'">课程资源</el-menu-item> -->
      <el-menu-item><a :href="forumLink" target="_blank">答疑平台</a>
      </el-menu-item>
      <el-submenu index="older" router>
        <template slot="title">过往学期</template>
        <el-menu-item :index="$router.path"
          v-for="(course, i) in allinfo.series_courses" :key="i">
          <el-link :href="'/course/' + course.cid + '/home'"
            style="display:block;text-align:center;" :underline="false">
            {{ course.name_zh + course.semester }}
          </el-link>
        </el-menu-item>
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
  computed: {
    forumLink() {
      const appPath = window.location.href.match(/http:\/\/[^/]*\//)[0];
      return `${appPath}proans/course/${this.$route.params.cid}`;
    },
  },
};
</script>

<style scoped>
.el-menu {
  display: flex;
  justify-content: flex-end;
}

.el-menu-item {
  line-height: 55px !important;
}

.el-submenu {
  padding-right: 2em;
}

.el-submenu .el-menu-item {
  display: flex;
  justify-content: center;
}

a {
  text-decoration: none;
}
</style>
