<template>
  <div>
    <!-- This is TeacherCourseList component. -->
    <el-row :gutter="40">
      <el-col :span="8" v-for="(item, i) in courses" :key="i">
        <router-link :to="'/teacher/1/course/1/semesters'">
          <el-button type="primary" plain>
              {{item.name}}
          </el-button>
        </router-link>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'CourseListView',
  computed: {
    courses() {
      console.log(this.$store.getters.getDistinctCourses);
      return this.$store.getters.getDistinctCourses;
    },
  },
  beforeCreate() {
    this.$store.dispatch('initCoursesForTeacher');
  },
};
</script>

<style scoped>
.el-row {
  width: 1000px;

}
.el-button {
  height: 120px;
  width: 100%;
  font-size: 20px;
  margin-bottom: 30px;
}
</style>
