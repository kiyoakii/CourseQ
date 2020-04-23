<template>
  <div>
    <el-card class="box-card">
      <div id="course-info" >
        <div id="course-name">
          <h1>{{ courseName }}</h1>
          <p>{{ semester }}</p>
        </div>
        <div id="course-intro">
          <p>{{ introduction }}</p>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CourseInfo',
  props: {
    courseName: {
      type: String,
      default: 'CourseName',
    },
    semester: {
      type: String,
      default: '2020Spring',
    },
    introduction: {
      type: String,
      default: 'Introduction...',
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
