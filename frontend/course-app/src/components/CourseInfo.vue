<template>
  <div>
    <el-card class="box-card">
      <div id="course-info" >
        <div id="course-name">
          <h1>{{ courseInfo.name }}</h1>
          <p>{{ courseInfo.semester }}</p>
        </div>
        <div id="course-intro">
          <p>{{ courseInfo.intro }}</p>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CourseInfo',
  props: {
    courseInfo: {
      type: Object,
      default() {
        return {
          name: 'CourseName',
          semester: '2020Spring',
          intro: 'Introduction...',
        };
      },
    },
  },
};
</script>

<style scoped>
#course-info {
  display: flex;
  flex-direction: row;
  height: 200px;
}
#course-name {
  flex: 2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#course-name > h1 {
  margin: 0;
}
#course-intro {
  flex: 4;
  text-align: left;
}
</style>
