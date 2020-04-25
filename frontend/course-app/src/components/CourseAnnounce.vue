<template>
  <div>
    <!-- This is CourseAnnounce view. -->
    <el-card>
      <div slot="header" class="announcement-info">
        <h1>Announcements</h1>
      </div>
    <el-card  shadow="always" class="announcement-card">
      <div slot="header" class="announcement-info">
        <h3 class="announcement-title">{{ Announcements[0].title }}</h3>
        <div class="announcement-publish-info">
          发布者：{{ Announcements[0].publisher }}
        </div>
        <div class="announcement-publish-info">
          发布时间：{{ Announcements[0].time }}
        </div>
      </div>
      <div class="announcement-content">
        {{ Announcements[0].content }}
      </div>
    </el-card>
    <el-collapse>
      <el-collapse-item name="1">
        <template slot="title">
          <h1 class="more-announcements-header">More</h1>
        </template>
        <el-scrollbar class="announcements-panel">
          <el-card v-for="item in Announcements.slice(1)" :key="item.title"
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
    </el-card>
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
          {
            title: 'Announcement 3',
            publisher: 'teacher 3',
            time: '2020:04:25 20:00',
            content: 'Announcement 3 content ...',
          },
          {
            title: 'Announcement 4',
            publisher: 'teacher 4',
            time: '2020:04:25 20:00',
            content: 'Announcement 4 content ...',
          },
          {
            title: 'Announcement 5',
            publisher: 'teacher 5',
            time: '2020:04:25 20:00',
            content: 'Announcement 5 content ...',
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

.announcements-panel {
  width: 100%;
  height: 30em;
}

.announcement-info {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-items: baseline
}

.more-announcements-header {
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
