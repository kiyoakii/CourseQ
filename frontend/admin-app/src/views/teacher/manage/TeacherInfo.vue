<template>
  <div>
    <h2>教师信息</h2>
    <div id="flex-bar">
      <div class="flex-item">
        <data-table-search-bar
          v-model="searchText">
        </data-table-search-bar>
      </div>
      <div class="flex-item">
        <el-button type="primary" @click="create">添加教师</el-button>
      </div>
    </div>
    <el-dialog
      :title="'添加'"
      :visible.sync="dialogVisible"
      width="1000px">
      <div id="flex-bar">
        <div>
          <data-table-search-bar
            v-model="searchTextD">
          </data-table-search-bar>
        </div>
      </div>
      <div class="table">
        <data-table
          :memberData="allTeachers"
          :tableFormat="memberTable"
          @delete="deleteRow"
          :actionFormat="'select'"
          :searchText="searchTextD"
          v-model="selectedStus">
        </data-table>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
    <data-table
      :memberData="memberFilter(allInfo.teachers)"
      :tableFormat="memberTable"
      @delete="deleteRow"
      :searchText="searchText">
    </data-table>
  </div>
</template>

<script>
import DataTableSearchBar from '@/components/DataTableSearchBar.vue';
import DataTable from '@/components/DataTable.vue';
import { memberTable } from '@/helpers/table';
import { memberFilter } from '@/helpers/filters';

export default {
  name: 'TeacherAssiList',
  components: {
    DataTable,
    DataTableSearchBar,
  },
  props: {
    allInfo: {},
  },
  data() {
    return {
      searchText: '',
      searchTextD: '',
      memberTable,
      memberFilter,
      selectedStus: [],
      form: {
        id: '',
        name: '',
        email: '',
        phone: '',
        school: '',
      },
      dialogVisible: false,
    };
  },
  computed: {
    allTeachers() {
      return this.$store.getters.adminAllTeachers;
    },
  },
  beforeCreate() {
    this.$store.dispatch('initAllTeachers');
  },
  methods: {
    deleteRow() {
      console.log('edit!');
    },
    submit() {
      console.log('submit');
    },
    create() {
      this.form = {
        id: '',
        name: '',
        email: '',
        phone: '',
        school: '',
      };
      this.dialogVisible = true;
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
}
#ta-search {
  margin: 10px 0;
}

#table {
  display: flex;
}

</style>
