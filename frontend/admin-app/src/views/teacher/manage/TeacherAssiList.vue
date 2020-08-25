<template>
  <div>
    <h2 id="title">助教名单</h2>
    <div id="flex-bar">
      <div class="flex-item">
        <data-table-search-bar
          v-model="searchText">
        </data-table-search-bar>
      </div>
      <div class="flex-item">
        <el-button type="primary" @click="create">添加助教</el-button>
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
          :memberData="allStudents"
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
      :memberData="memberFilter(allInfo.assistants)"
      :tableFormat="memberTable"
      :actionFormat="'delete'"
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
import { instance } from '@/helpers/instances';

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
    allStudents() {
      return this.$store.getters.adminAllStudents;
    },
  },
  beforeCreate() {
    this.$store.dispatch('initAllStudents');
  },
  methods: {
    deleteRow(row) {
      this.$confirm('确认刪除？')
        .then(() => {
          const data = {
            name_zh: this.allInfo.name_zh,
            name_en: this.allInfo.name_en,
            intro: this.allInfo.intro,
            series: this.allInfo.series,
            pre_course: '',
            textbooks: this.allInfo.textbooks,
            semester: this.allInfo.semester,
            new_teachers_gid: [],
            new_students_gid: [],
            new_TAs_gid: [],
            del_teachers_gid: [],
            del_students_gid: [],
            del_TAs_gid: [],
          };
          data.del_TAs_gid.push(row.id);
          instance.patch(`/api/v1/courses/${this.$route.params.cid}`,
            data)
            .then((res) => {
              console.log(res);
              this.dialogVisible = false;
              this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
            });
        });
    },
    submit() {
      console.log(this.selectedStus);
      const data = {
        name_zh: this.allInfo.name_zh,
        name_en: this.allInfo.name_en,
        intro: this.allInfo.intro,
        series: this.allInfo.series,
        pre_course: '',
        textbooks: this.allInfo.textbooks,
        semester: this.allInfo.semester,
        new_teachers_gid: [],
        new_students_gid: [],
        new_TAs_gid: [],
        del_teachers_gid: [],
        del_students_gid: [],
        del_TAs_gid: [],
      };
      this.selectedStus.forEach((stu) => {
        if (!this.allInfo.assistants.find((item) => item.gid === stu.id)) {
          data.new_TAs_gid.push(stu.id);
        }
      });
      instance.patch(`/api/v1/courses/${this.$route.params.cid}`,
        data)
        .then((res) => {
          console.log(res);
          this.dialogVisible = false;
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
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
#title {
  margin-top: 20px;
}
#flex-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  margin-top: 20px;
}
#ta-search {
  margin: 10px 0;
}

#table {
  display: flex;
}

</style>
