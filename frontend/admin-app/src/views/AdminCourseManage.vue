<template>
  <div class="course-manage">
    <!-- This is AdminCourseManage component. -->
    <h2>课程列表</h2>
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
        <el-col :span="6" v-for="(item, i) in courses" :key="i">
            <el-button type="primary" class="course-button" plain
              @click="openModify(item)">
                {{item.courseName}}
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
        <span>课程信息修改</span>
      </div>
      <div class="drawer__content">
        <el-form ref="form" :model="form">
          <el-form-item label="课程标题">
            <el-input v-model="form.courseName"></el-input>
          </el-form-item>
          <el-form-item label="主讲教师">
            <el-input v-model="form.lecturerName"></el-input>
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
        <span>开设新课程</span>
      </div>
      <div class="drawer__content">
        <el-form ref="form" :model="form">
          <el-form-item label="课程标题">
            <el-input v-model="form.courseName"></el-input>
          </el-form-item>
          <el-form-item label="主讲教师">
            <el-input v-model="form.lecturerName"></el-input>
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
  name: 'AdminCourseManage',
  components: {
    AdminCourseListSearch,
  },
  props: {
    courses: {
      type: Array,
      default() {
        return [
          {
            courseName: '软件工程',
            lecturerName: '李京',
            link: '1',
          },
          {
            courseName: '计算方法',
            lecturerName: '陈先进',
            link: '2',
          },
          {
            courseName: '人工智能',
            lecturerName: '吉建民',
            link: '3',
          },
          {
            courseName: '体系结构',
            lecturerName: '张燕咏',
            link: '4',
          },
        ];
      },
    },
  },
  data() {
    return {
      infoManageActive: false,
      newCourseActive: false,
      form: {
        courseName: '软件工程',
        lecturerName: '李京',
      },
      loading: false,
    };
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
      this.form.lecturerName = course.lecturerName;
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
