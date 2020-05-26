<template>
  <div class="course-manage">
    <!-- This is AdminCourseManage component. -->
    <div class="course-manage-header">
      <h2>课程列表</h2>
    </div>
    <div class="course-manage-content">
      <div id="flex-bar">
        <div class="flex-item">
          <admin-course-list-search id="course-search"></admin-course-list-search>
        </div>
        <div class="flex-item">
            <el-button type="primary" @click="newCourseActive = true">开设课程</el-button>
        </div>
      </div>
      <el-row :gutter="40">
        <el-col :span="6" v-for="course in courses" :key="course.id">
            <el-button type="primary" class="course-button" plain
              @click="openModify(course)">
                {{course.courseName}}
            </el-button>
        </el-col>
      </el-row>
    </div>
    <el-drawer
      :before-close="handleClose"
      :visible.sync="infoManageActive"
      direction="rtl"
      class="drawer"
      ref="drawer"
      >
      <div slot="title">
        <h1>课程信息修改</h1>
      </div>
      <div class="drawer__content">
        <el-form ref="form" :model="form">
          <el-form-item label="课程标题">
            <el-input v-model="form.courseName"></el-input>
          </el-form-item>
          <el-form-item label="主讲教师">
            <el-input v-model="form.teacherName"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <div class="drawer-control">
            <el-button type="primary" @click="onSubmit"
              :loading="loading">{{ loading ? '提交中 ...' : '提 交' }}</el-button>
            <el-button @click="cancelForm">取 消</el-button>
          </div>
          <el-button type="danger" class="btn-delete-course">删除课程</el-button>
        </div>
      </div>
    </el-drawer>
    <el-drawer
      :before-close="handleClose"
      :visible.sync="newCourseActive"
      direction="rtl"
      class="drawer"
      ref="drawer"
      >
      <div slot="title">
        <h1>开设新课程</h1>
      </div>
      <div class="drawer__content">
        <el-form ref="form" :model="form">
          <el-form-item label="课程标题">
            <el-input v-model="form.courseName"></el-input>
          </el-form-item>
          <el-form-item label="主讲教师">
            <el-input v-model="form.teacherName"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <div class="drawer-control">
            <el-button type="primary" @click="onSubmit"
              :loading="loading">{{ loading ? '提交中 ...' : '提 交' }}</el-button>
            <el-button @click="cancelForm">取 消</el-button>
          </div>
      </div>
      </div>
    </el-drawer>

  </div>
</template>

<script>
import AdminCourseListSearch from '@/components/AdminCourseListSearch.vue';

export default {
  name: 'CourseManage',
  components: {
    AdminCourseListSearch,
  },
  data() {
    return {
      infoManageActive: false,
      newCourseActive: false,
      form: {
        courseName: '软件工程',
        teacherName: '李京',
      },
      loading: false,
      courses: [],
    };
  },
  mounted() {
    this.axios.get('/v1/admin/admin/course-list')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.courses = res.data.courses;
      });
  },
  methods: {
    onSubmit() {
      if (this.loading) {
        return;
      }
      this.$confirm('确定要提交表单吗？')
        .then(() => {
          this.loading = true;
          this.timer = setTimeout(() => {
            // 动画关闭需要一定的时间
            setTimeout(() => {
              this.loading = false;
              this.infoManageActive = false;
              this.newCourseActive = false;
            }, 400);
          }, 2000);
        })
        .catch(() => {
        });
    },
    onDeleteCourse() {
      console.log('Delete course!');
    },
    openModify(course) {
      this.infoManageActive = true;
      this.form.courseName = course.courseName;
      this.form.teacherName = course.teacherName;
    },
    handleClose(done) {
      if (this.loading) {
        return;
      }
      this.$confirm('确定要提交表单吗？')
        .then(() => {
          this.loading = true;
          this.timer = setTimeout(() => {
            done();
            // 动画关闭需要一定的时间
            setTimeout(() => {
              this.loading = false;
            }, 400);
          }, 2000);
        })
        .catch(() => {
          this.loading = false;
          this.infoManageActive = false;
          this.newCourseActive = false;
          clearTimeout(this.timer);
        });
    },
    cancelForm() {
      this.loading = false;
      this.infoManageActive = false;
      this.newCourseActive = false;
      clearTimeout(this.timer);
    },
  },
};
</script>

<style scoped>
.course-manage {
  flex: 1;
  padding: 30px;
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
#flex-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
}
#course-search {
  margin: 10px 0;
}
.course-button {
  height: 120px;
  width: 100%;
  font-size: 20px;
  margin-bottom: 30px;
}
.drawer__content {
  flex: 1;
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 20px;
}
form {
  flex: 1;
  margin-top: 0em;
}
.el-form-item {
  display: flex;
}
.drawer__footer {
  display: flex;
}
.drawer-control {
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.drawer-control button {
  flex: 1;
  margin: 0 10px;
}

</style>
