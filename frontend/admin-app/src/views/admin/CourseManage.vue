<template>
  <el-row class="course-manage" type="flex" justify="center">
    <el-col :md="24" :lg="23">
      <el-row type="flex" justify="space-between" class="mb-4">
        <div style="width: 250px">
          <data-table-search-bar
            v-model="searchText">
            </data-table-search-bar>
        </div>
        <div>
          <el-button type="primary" @click="create">开设新课程</el-button>
        </div>
      </el-row>
      <el-row>
        <data-table
          :memberData="allCourses"
          :tableFormat="courseTable"
          @delete="deleteRow"
          @edit="editRow"
          :searchText="searchText">
        </data-table>
      </el-row>
    </el-col>
    <el-dialog
      :title="form.id === '' ? '添加' : '编辑'"
      :visible.sync="dialogVisible"
      width="720px">
      <el-row type="flex" justify="center">
        <el-col :span="20">
          <el-form label-position="left" label-width="140px"
            :model="form" :rules="rules" ref="form">
            <el-form-item label="ID" v-show="form.id !== ''">
              <el-input v-model="form.id" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="课程名称(中)" prop="name_zh">
              <el-input v-model="form.name_zh"></el-input>
            </el-form-item>
            <el-form-item label="课程名称(英)" prop="name_en">
              <el-input v-model="form.name_en"></el-input>
            </el-form-item>
            <el-form-item label="课程介绍" prop="intro">
              <el-input v-model="form.intro"></el-input>
            </el-form-item>
            <el-form-item label="学期" prop="semester">
              <el-input v-model="form.semester"></el-input>
            </el-form-item>
            <el-form-item label="系列" prop="series">
              <el-input v-model="form.series"></el-input>
            </el-form-item>
            <el-form-item label="预修课程" prop="pre_course">
              <el-input v-model="form.pre_course"></el-input>
            </el-form-item>
            <el-form-item label="教科书" prop="textbooks">
              <el-input v-model="form.textbooks"></el-input>
            </el-form-item>
            <el-form-item label="授课教师" prop="teachers_gid">
              <el-select v-model="form.teachers_gid" filterable multiple
                placeholder="请选择"
                style="width: 100%;">
                <el-option
                  v-for="item in teacherOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit(form.id)">确 定</el-button>
      </span>
    </el-dialog>
  </el-row>
</template>

<script>
import DataTableSearchBar from '@/components/DataTableSearchBar.vue';
import DataTable from '@/components/DataTable.vue';
import { instance } from '@/helpers/instances';
import { courseTable } from '@/helpers/table';

export default {
  name: 'CourseManage',
  components: {
    DataTableSearchBar,
    DataTable,
  },
  data() {
    return {
      searchText: '',
      originalTeachersGid: [],
      courseTable,
      form: {
        id: '',
        name_zh: '',
        name_en: '',
        intro: '',
        pre_course: '',
        textbooks: '',
        semester: '',
        series: '',
        teachers_gid: [],
      },
      dialogVisible: false,
      rules: {
        name_zh: [
          { required: true, message: '请输入课程名称（中）', trigger: ['change', 'blur'] },
        ],
        name_en: [
          { required: true, message: '请输入课程名称（英）', trigger: ['change', 'blur'] },
        ],
        textbooks: [
          { required: true, message: '请输入教科书名称', trigger: ['change', 'blur'] },
        ],
        semester: [
          { required: true, message: '请输入学期', trigger: ['change', 'blur'] },
        ],
        series: [
          { required: true, message: '请输入系列', trigger: ['change', 'blur'] },
        ],
        teachers_gid: [
          { required: true, message: '请选择至少一位教师', trigger: ['change', 'blur'] },
        ],
      },
    };
  },
  computed: {
    allCourses() {
      return this.$store.getters.adminAllCourses;
    },
    teacherOptions() {
      return this.$store.getters.teacherOptions;
    },
  },
  beforeCreate() {
    this.$store.dispatch('initAllCourses');
    this.$store.dispatch('initAllTeachers');
  },
  methods: {
    diff(oldArray, newArray) {
      const newItems = [];
      const delItems = [];
      newArray.forEach((item) => {
        if (!oldArray.includes(item)) {
          newItems.push(item);
        }
      });
      oldArray.forEach((item) => {
        if (!newArray.includes(item)) {
          delItems.push(item);
        }
      });
      return { newItems, delItems };
    },
    submit(id) {
      this.$refs.form.validate((valid) => {
        if (!valid) {
          this.$message.error('请正确填写完表格再提交！');
          return;
        }
        let options = {};
        if (id === '') {
          options = {
            url: '/api/v1/courses',
            method: 'post',
            data: {
              ...this.form,
            },
          };
        } else {
          const { newItems, delItems } = this.diff(this.originalTeachersGid,
            this.form.teachers_gid);
          console.log(111, newItems);
          options = {
            url: `/api/v1/courses/${id}`,
            method: 'patch',
            data: {
              ...this.form,
              new_teachers_gid: newItems,
              del_teachers_gid: delItems,
            },
          };
        }
        instance(options).then((res) => {
          if (res.status !== 200) {
            return;
          }
          this.$store.dispatch('initAllCourses');
        }).catch((err) => {
          console.log(err);
        });
        this.dialogVisible = false;
      });
    },
    create() {
      this.form = {
        id: '',
        name_zh: '',
        name_en: '',
        intro: '',
        pre_course: '',
        textbooks: '',
        semester: '',
        series: '',
        teachers_gid: [],
      };
      this.originalTeachersGid = [];
      this.dialogVisible = true;
    },
    editRow(row) {
      const course = this.$store.getters.getCourseByID(row.id);
      this.originalTeachersGid = course.teachers.reduce((teachers, teacher) => {
        teachers.push(teacher.gid);
        return teachers;
      }, []);
      this.form = {
        id: course.cid,
        name_zh: course.name_zh,
        name_en: course.name_en,
        intro: course.intro,
        pre_course: course.pre_course,
        textbooks: course.textbooks,
        semester: course.semester,
        series: course.series,
        teachers_gid: [...this.originalTeachersGid],
      };
      this.dialogVisible = true;
    },
    deleteRow(row) {
      this.$confirm(`删除${row.name}-${row.id}?`, '提示', {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
        instance({
          url: `/api/v1/courses/${row.id}`,
          method: 'delete',
        }).then((res) => {
          if (res.status !== 204) {
            return;
          }
          this.$store.dispatch('initAllCourses');
        }).catch((err) => {
          // this.$message.error(`请求失败：${err.message}`);
          console.log(err);
        });
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除',
        });
      });
    },
  },
};
</script>

<style scoped>
.course-manage {
  flex: 1;
}
.course-manage-header {
  padding: 0 100px;
}
.course-manage-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 10px 200px;
}
.mb-4 {
  margin-bottom: 10px;
}

</style>
