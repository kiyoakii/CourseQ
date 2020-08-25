<template>
  <div>
    <el-row type="flex" justify="center">
      <el-table :data="tableData" border class="member-table" align="center">
        <template v-for="(col, index) in tableFormat">
          <el-table-column
            :key="index"
            :label="col.label"
            :prop="col.prop"
            align="center"
            :min-width="col.minWidth">
          </el-table-column>
        </template>
        <el-table-column align="center" min-width="160"
          :label="actionFormat === 'select'?'选择':'操作'">
          <template slot-scope="scope">
            <div v-if="actionFormat === 'normal'">
              <el-button
                size="mini"
                type="primary"
                @click="handleEdit(scope.row)">编辑</el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.row)">删除</el-button>
            </div>
            <div v-else-if="actionFormat === 'delete'">
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.row)">删除</el-button>
            </div>
            <el-checkbox v-else @change="handleSelect($event, scope.row)"></el-checkbox>
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
  model: {
    prop: 'selectedMems',
    event: 'updateSelectedMems',
  },
  props: {
    memberData: {
      type: Array,
    },
    searchText: {
      type: String,
      default: '',
    },
    tableFormat: {
      type: Array,
    },
    actionFormat: {
      type: String,
      default: 'normal',
    },
  },
  data() {
    return {
      currentPage: 1,
      pageSize: 10,
      mems: [],
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
    handleSelect(val, row) {
      if (val === true) {
        this.mems.push(row);
      } else {
        this.mems.splice(this.mems.findIndex((item) => item.id === row.id));
      }
      this.$emit('updateSelectedMems', this.mems);
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
