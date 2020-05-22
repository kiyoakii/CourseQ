<template>
  <div>
    <!-- This is TeacherInfo component. -->
    <h2>教师信息</h2>
    <div id="flex-bar">
      <div class="flex-item">
        <el-form :inline="true" :model="searchForm">
          <el-form-item class="form-item">
            <el-input v-model="searchForm.name" placeholder="姓名"></el-input>
          </el-form-item>
          <el-form-item class="form-item">
            <el-button type="primary" @click="onSearch">查询</el-button>
          </el-form-item>
        </el-form>
      </div>
      <div class="flex-item">
        <el-button type="primary" @click="onSubmit">添加教师</el-button>
      </div>
    </div>
    <el-table :data="teacherInfo" border id="teacher-table">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="email" label="邮箱"></el-table-column>
      <el-table-column prop="phone" label="电话"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'TeacherInfo',
  data() {
    return {
      teacherInfo: [
        {
          name: 'teacher1',
          email: 'email1',
          phone: 'phone1',
        },
        {
          name: 'teacher2',
          email: 'email2',
          phone: 'phone2',
        },
      ],
      searchForm: {
        name: '',
      },
    };
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    onSubmit() {
      console.log('submit!');
    },
  },
};
</script>

<style scoped>
#flex-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin: 10px 0;
}
#teacher-table{
  width: 800px;
}
.form-item {
  margin-bottom: 0;
}
</style>
