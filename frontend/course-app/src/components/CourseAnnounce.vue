<template>
  <div>
    <!-- This is CourseAnnounce view. -->
    <el-collapse value='1'>
      <el-collapse-item name="1">
        <template slot="title">
          <h1 class="announcements-header">Announcements</h1>
        </template>
        <el-scrollbar class="announcement-panel">
          <el-card v-for="item in Announcements" :key="item.title"
            shadow="always" class="announcement-card">
            <div slot="header" class="announcement-info">
              <h3 class="announcement-title">{{ item.title }}</h3>
              <div class="announcement-publish-info">
                发布者：{{ item.publisher }}
              </div>
              <div class="announcement-publish-info">
                发布时间：{{ item.time }}
              </div>
            </div>
            <div class="announcement-content">
              {{ item.content }}
            </div>
          </el-card>
        </el-scrollbar>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  props: {
    Announcements: {
      default() {
        return [
          {
            title: 'Announcement 1',
            publisher: 'teacher 1',
            time: '2020.04.25 20:00',
            content: 'Announcement 1 content ...',
          },
          {
            title: 'Announcement 2',
            publisher: 'teacher 2',
            time: '2020:04:25 20:00',
            content: 'Announcement 2 content ...',
          },
        ];
      },
    },
  },
};
</script>

<style scoped>

.announcement-card {
  margin-top: 1em;
}

.announcement-panel {
  width: 100%;
  height: 30em;
}

.announcement-info {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: baseline
}

.announcements-header {
  font-weight:700;
  margin-left: 1em;
}

.announcement-title {
  margin: 0 1em;
}

.announcement-publish-info {
 font-weight:200;
 margin:0 1em;
}

.announcement-content {
  margin:0 1em;
}

</style>
