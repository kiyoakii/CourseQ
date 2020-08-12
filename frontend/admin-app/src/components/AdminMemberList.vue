<template>
  <div>
    <el-row type="flex" justify="center">
      <el-table :data="tableData" border class="member-table" align="center">
        <el-table-column align="center" min-width="140" prop="id" label="ID"></el-table-column>
        <el-table-column align="center" min-width="100" prop="name" label="姓名"></el-table-column>
        <el-table-column align="center" min-width="200" prop="email" label="邮箱"></el-table-column>
        <el-table-column align="center" min-width="140" prop="phone" label="电话"></el-table-column>
        <el-table-column align="center" min-width="140"
          prop="school" label="所属院系"></el-table-column>
        <el-table-column align="center" min-width="160" label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="primary"
              @click="handleEdit(scope.row)">编辑</el-button>
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.row)">删除</el-button>
          </template>
        </el-table-column>
      </el-table>
    </el-row>

    <el-row type="flex" justify="center" class="mt-4">
      <el-pagination
        background
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="pageSize"
        layout="sizes, prev, pager, next, jumper"
        :total="filteredData.length">
      </el-pagination>
    </el-row>

  </div>
</template>

<script>
export default {
  name: 'AdminMemberList',
  props: {
    memberData: {
      type: Array,
    },
    searchText: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      currentPage: 1,
      pageSize: 10,
    };
  },
  computed: {
    filteredData() {
      if (this.searchText) {
        return this.memberData.filter((item) => {
          return Object.keys(item).some((key) => {
            return String(item[key]).toLowerCase().indexOf(this.searchText.toLowerCase()) > -1;
          });
        });
      }
      return this.memberData;
    },
    tableData() {
      return this.filteredData.slice((this.currentPage - 1) * this.pageSize,
        this.currentPage * this.pageSize);
    },
  },
  methods: {
    handleDelete(row) {
      this.$emit('delete', row);
    },
    handleEdit(row) {
      this.$emit('edit', row);
    },
    handleSizeChange(val) {
      this.pageSize = val;
    },
    handleCurrentChange(val) {
      this.currentPage = val;
    },
  },
};
</script>

<style scoped>
.member-table {
  flex: 1;
}
.mt-4 {
  margin-top: 10px;
}
</style>
