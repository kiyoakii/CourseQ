<template>
  <div>
    <el-breadcrumb class="navbar" separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{'path': '/teacher/course-list'}"
      v-if="isCourseList || isSemesterList || isCourse">课程列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/semester-list'}"
      v-if="isSemesterList || isCourse">学期列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{'path': '/teacher/course'}"
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
      return this.$route.path === '/teacher/course-list';
    },
    isSemesterList() {
      return this.$route.path === '/teacher/semester-list';
    },
    isCourse() {
      return this.$route.path.indexOf('/teacher/course/') !== -1;
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
