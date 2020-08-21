<template>
  <div>
    <el-breadcrumb class="navbar" separator-class="el-icon-arrow-right">
      <el-breadcrumb-item :to="{'path': `/teacher/${$route.params.tid}/courses`}"
      v-if="isCourseList || isSemesterList || isCourse">课程列表</el-breadcrumb-item>
      <el-breadcrumb-item :to="{
        'path': `/teacher/${$route.params.tid}/course/${$route.params.cname}/semesters`}"
      v-if="isSemesterList || isCourse">学期列表</el-breadcrumb-item>
      <el-breadcrumb-item
      v-if="isCourse">{{ courseName }}</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: 'TeacherNavBar',
  data() {
    return {
    };
  },
  computed: {
    isCourseList() {
      const re = /\/teacher\/\d+\/courses/;
      return re.test(this.$route.path);
    },
    isSemesterList() {
      const re = /\/teacher\/\d+\/course\/.+\/semesters/;
      return re.test(this.$route.path);
    },
    isCourse() {
      const re = /\/teacher\/\d+\/course\/.+\/semester\/.+\/manage\/.*/;
      return re.test(this.$route.path);
    },
    courseName() {
      return this.$store.getters.getCourseNameByID(this.$route.params.cid);
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
