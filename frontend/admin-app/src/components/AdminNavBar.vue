<template>
  <div>
    <el-menu default-active="/admin/course-manage" class="el-menu-demo"
    mode="horizontal" router>
      <el-menu-item index="/admin/course-manage">课程管理</el-menu-item>
      <el-menu-item index="/admin/teacher-manage">教师管理</el-menu-item>
      <el-menu-item index="/admin/student-manage">学生管理</el-menu-item>
    </el-menu>
  </div>
</template>

<script>
export default {
  name: 'AdminNavBar',
};
</script>

<style scoped>
</style>
