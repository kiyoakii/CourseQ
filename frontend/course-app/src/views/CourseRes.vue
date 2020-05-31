<template>
  <div id="course-resourse">
    <!-- This is CourseRes view. -->
    <div class="header">
      <h1>Resourses</h1>
    </div>
    <el-card v-for="(item, i) in allinfo.resourses" :key="i">
      <div slot="header" class="res-header">
        <h3 class="title">{{ item.title }}</h3>
        <div class="date">
          {{ item.date }}
        </div>
      </div>
      <div class="resourse-content" v-for="(attachment, j) in item.attachments" :key="j">
        <el-link :href="attachment.downloadLink">{{ attachment.name }}</el-link>
      </div>
    </el-card>
    <div v-if="resourses.length == 0">
      暂时没有课程资源，请等待老师上传
    </div>
  </div>
</template>

<script>
export default {
  name: 'CourseRes',
  props: {
    allinfo: {},
  },
};
</script>

<style scoped>
#course-resourse > * {
  margin-bottom: 30px;
}
.res-header {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: baseline;
}
.title {
  margin: 0 1em;
}
.date {
   margin: 0 1em;
   color: #909399;
}
.resourse-content {
  margin: 0 1em;
}

</style>
