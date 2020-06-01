<template>
  <div>
    <!-- This is TeacherSemesterList component. -->
    <el-row :gutter="40">
      <el-col :span="8" v-for="(item, i) in semesters" :key="i">
        <router-link :to="'/teacher/1/course/1/semester/1/manage/assistants'">
          <el-button type="primary" plain>
              {{item.name}}
          </el-button>
        </router-link>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'SemesterListView',
  data() {
    return {
      semesters: [],
    };
  },
  mounted() {
    this.axios.get('/v1/admin/teacher/semester-list?course=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.semesters = res.data.semesters;
      });
  },
};
</script>

<style scoped>
.el-row {
  width: 1000px;

}
.el-button {
  height: 120px;
  width: 100%;
  font-size: 20px;
  margin-bottom: 30px;
}
</style>
