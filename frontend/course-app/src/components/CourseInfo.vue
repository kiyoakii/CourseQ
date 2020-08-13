<template>
  <div>
    <el-card class="box-card">
      <div id="course-info" >
        <div id="course-name">
          <h1>{{ allinfo.name_zh }}</h1>
          <p>{{ allinfo.name_en }}</p>
          <p>{{ allinfo.semester }}</p>
        </div>
        <div id="course-intro">
          <p>{{ allinfo.intro }}</p>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CourseInfo',
  props: {
    allinfo: {},
  },
};
</script>

<style scoped>
#course-info {
  display: flex;
  flex-direction: row;
  height: 200px;
  align-items: center;
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
