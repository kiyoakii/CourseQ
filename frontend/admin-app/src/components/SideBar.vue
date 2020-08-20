<template>
  <div class="list">
    <div v-for="item in list" :key="item.name">
    <el-card class="list-item" :class="$route.name === item.link ? 'is-always-shadow' : ''"
      align="center" shadow="hover">
      <router-link :to="item.link" class="link">
        {{ item.name }}
      </router-link>
    </el-card>
    </div>
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
          name: '课程日历',
          link: 'schedule',
        },
      ],
      current: this.$route.name,
    };
  },
  methods: {
    testRouter() {
      console.log(this.$route.name);
    },
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
