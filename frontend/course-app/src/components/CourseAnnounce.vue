<template>
  <div>
    <!-- This is CourseAnnounce view. -->
    <el-card shadow="always">
      <div slot="header" class="announcement-info">
        <h1>Announcements</h1>
      </div>
      <el-card v-if="announcements.length > 0" shadow="always" class="announcement-card">
        <div slot="header" class="announcement-info">
          <h3 class="announcement-title">{{ announcements[0].title }}</h3>
          <div class="announcement-publish-info">
            发布者：{{ announcements[0].publisher }}
          </div>
          <div class="announcement-publish-info">
            发布时间：{{ announcements[0].time }}
          </div>
        </div>
        <div class="announcement-content">
          {{ announcements[0].content }}
        </div>
      </el-card>
      <div v-else>暂时没有公告哦(*^__^*)</div>
      <el-collapse v-if="announcements.length > 1">
        <el-collapse-item name="1">
          <template slot="title">
            <h1 class="more-announcements-header">More</h1>
          </template>
          <el-scrollbar class="announcements-panel">
            <el-card v-for="item in announcements.slice(1)" :key="item.title"
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
    announcements: {
      type: Array,
      default() {
        return [];
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
