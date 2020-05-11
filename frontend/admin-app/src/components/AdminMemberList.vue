<template>
  <div>
    <el-table :data="memberData" border id="member-table">
      <el-table-column prop="name" label="姓名"></el-table-column>
      <el-table-column prop="id" label="学号"></el-table-column>
      <el-table-column prop="email" label="邮箱"></el-table-column>
      <el-table-column prop="phone" label="电话"></el-table-column>
      <el-table-column prop="academy" label="所属院系"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">注销</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'AdminMemberList',
  props: {
    memberData: {
      type: Array,
      default() {
        return [
          {
            name: 'name1',
            id: 'id1',
            email: 'email1',
            phone: 'phone1',
            academy: 'Computer Science',
          },
          {
            name: 'name2',
            id: 'id2',
            email: 'email2',
            phone: 'phone2',
            academy: 'Computer Science',
          },
          {
            name: 'name3',
            id: 'id3',
            email: 'email3',
            phone: 'phone3',
            academy: 'Computer Science',
          },
        ];
      },
    },
  },
  methods: {
    handleDelete(index, row) {
      console.log(index, row);
    },
  },
};
</script>

<style scoped>
#member-table {
  width: 1000px;
}
</style>
