<template>
  <div>
    <el-breadcrumb class="navbar" separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{'path': '/teacher/course-list'}">课程列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/semester-list'}">2019年春</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/course'}">计算方法</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'TeacherNavBar',
};
</script>

<style scoped>
.navbar {
  height: 60px;
  line-height: 60px;
  font-size: 14px;
}
</style>
