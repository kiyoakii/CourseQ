<template>
  <div class="list">
    <el-card class="list-item" v-for="item in list" :key="item.name" align="center" shadow="hover">
      <router-link :to="item.link" class="link">
        {{ item.name }}
      </router-link>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'SideBar',
  data() {
    return {
      list: [
        {
          name: '助教管理',
          link: 'assistants',
        },
        {
          name: '学生管理',
          link: 'students',
        },
        {
          name: '课程简介',
          link: 'intro',
        },
        {
          name: '课程公告',
          link: 'announce',
        },
        {
          name: '课程作业',
          link: 'assignment',
        },
        {
          name: '课程资源',
          link: 'resource',
        },
        {
          name: '课程日历',
          link: 'schedule',
        },
        {
          name: '教师信息',
          link: 'teacher',
        },
        {
          name: '主⻚布局',
          link: 'layout',
        },
      ],
    };
  },
};
</script>

<style scoped>
.list {
  width: 200px;
  margin-right: 30px;
}
.list-item {
  margin-bottom: 10px;
}
.link {
  text-decoration: none;
  color: #303133;
}
</style>
