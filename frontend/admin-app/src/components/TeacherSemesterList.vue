<template>
  <div>
    <!-- This is TeacherSemesterList component. -->
    <el-row :gutter="40">
      <el-col :span="8" v-for="(item, i) in semesters" :key="i">
        <router-link :to="'/teacher/' + item.link">
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
  name: 'TeacherSemesterList',
  props: {
    semesters: {
      type: Array,
      default() {
        return [
          {
            name: '2019年春',
            link: 'course',
          },
          {
            name: '2018年春',
            link: '2',
          },
          {
            name: '2017年春',
            link: '3',
          },
          {
            name: '2016年春',
            link: '4',
          },
        ];
      },
    },
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
