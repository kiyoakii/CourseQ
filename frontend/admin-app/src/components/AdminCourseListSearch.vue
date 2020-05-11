<template>
  <div>
    <el-form :inline="true" :model="searchForm">
      <el-form-item class="form-item">
        <el-input v-model="searchForm.courseName" placeholder="课程名称"></el-input>
      </el-form-item>
      <el-form-item class="form-item">
        <el-input v-model="searchForm.teacherName" placeholder="教师名称"></el-input>
      </el-form-item>
      <el-form-item class="form-item">
        <el-button type="primary" @click="onSubmit">搜索</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'AdminCourseListSearch',
  data() {
    return {
      searchForm: {
        courseName: '',
        teacherName: '',
      },
    };
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },
  },
};
</script>

<style scoped>
.form-item {
  margin-bottom: 0;
}
</style>
