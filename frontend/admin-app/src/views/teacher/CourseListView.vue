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
  props: {
    courses: {
      type: Array,
      default() {
        return [
          {
            name: '计算方法',
            link: 'course',
          },
          {
            name: '计算方法',
            link: '2',
          },
          {
            name: '计算方法',
            link: '3',
          },
          {
            name: '计算方法',
            link: '4',
          },
        ];
      },
    },
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
