<template>
  <div>
    <el-menu default-active="/admin/1/courses" class="el-menu-demo"
    mode="horizontal" router>
      <el-menu-item index="/admin/1/courses">课程管理</el-menu-item>
      <el-menu-item index="/admin/1/teachers">教师管理</el-menu-item>
      <el-menu-item index="/admin/1/students">学生管理</el-menu-item>
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
