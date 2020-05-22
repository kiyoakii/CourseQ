<template>
  <div>
    <el-breadcrumb class="navbar" separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{'path': '/teacher/1/courses'}"
      v-if="isCourseList || isSemesterList || isCourse">课程列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/1/course/1/semesters'}"
      v-if="isSemesterList || isCourse">学期列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/1/course/1/semester/1/manage'}"
      v-if="isCourse">计算方法</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'TeacherNavBar',
  data() {
    return {
      // isCourseList: true,
      // isSemesterList: false,
      // isCourse: false,
    };
  },
  computed: {
    isCourseList() {
      return this.$route.path === '/teacher/1/courses';
    },
    isSemesterList() {
      return this.$route.path === '/teacher/1/course/1/semesters';
    },
    isCourse() {
      return this.$route.path.indexOf('/teacher/1/course/1/semester/1/manage') !== -1;
    },
  },
};
</script>

<style scoped>
.navbar {
  height: 60px;
  line-height: 60px;
  font-size: 14px;
}
</style>
