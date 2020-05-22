<template>
  <div class="course-announce">
    <el-row class="announce" v-for="anno in announceList" :key="anno.id">
      <el-card class="card-box">
        <div slot="header" class="clearfix card-header">
          <span>{{ anno.title }}</span>
          <el-button type="primary"
          icon="el-icon-edit" size="small">
          </el-button>
        </div>
        <div>
          {{ anno.content }}
        </div>
      </el-card>
    </el-row>
    <el-row>
      <el-button type="primary">新建公告</el-button>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  data() {
    return {
      announceList: [
        {
          title: 'Announcement1',
          content: 'This is Announcement1, This is Announcement1, This is Announcement1, This is Announcement1',
          id: 1,
        },
        {
          title: 'Announcement2',
          content: 'This is Announcement1, This is Announcement1, This is Announcement1, This is Announcement1',
          id: 2,
        },
        {
          title: 'Announcement2',
          content: 'This is Announcement1, This is Announcement1, This is Announcement1, This is Announcement1',
          id: 3,
        },
      ],
    };
  },
};
</script>

<style>
.announce {
  margin-bottom: 15px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
