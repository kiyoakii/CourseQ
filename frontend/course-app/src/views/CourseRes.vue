<template>
  <div id="course-resourse">
    <!-- This is CourseRes view. -->
    <div class="header">
      <h1>Resourses</h1>
    </div>
    <el-card v-for="(item, i) in resourses" :key="i">
      <div slot="header" class="res-header">
        <h3 class="title">{{item.title}}</h3>
        <div class="time">
          {{item.time}}
        </div>
      </div>
      <div class="resourse-content" v-for="(content, j) in item.content" :key="j">
        <el-link :href="content.link">{{content.name}}</el-link>
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
  data() {
    return {
      resourses: [
        {
          title: 'Resourse 1',
          time: '2020.04.27 20:00',
          content: [
            {
              name: 'resourse1.1',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
            {
              name: 'resourse1.2',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
          ],
        },
        {
          title: 'Resourse 2',
          time: '2020.04.27 20:00',
          content: [
            {
              name: 'resourse2.1',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
            {
              name: 'resourse2.2',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
          ],
        },
        {
          title: 'Resourse 3',
          time: '2020.04.27 20:00',
          content: [
            {
              name: 'resourse3.1',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
            {
              name: 'resourse3.2',
              link: 'https://element.eleme.cn/#/zh-CN/component/link',
            },
          ],
        },
      ],
    };
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
.time {
   margin: 0 1em;
   color: #909399;
}
.resourse-content {
  margin: 0 1em;
}

</style>
