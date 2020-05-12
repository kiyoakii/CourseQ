<template>
  <div class="course-announcement">
    <!-- This is CourseAnnounce view. -->
    <el-scrollbar>
        <el-card v-if="announcements.length > 0"
          shadow="always" class="announcement-card">
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
      <div v-if="announcements.length > 1"
        v-bind:class="{'announcements-panel-active': this.isActive,
        'announcements-panel-close': !this.isActive}">
        <transition-group name="fade">
          <el-card v-show="isActive" v-for="item in announcements.slice(1)" :key="item.title"
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
        </transition-group>
      </div>
    </el-scrollbar>
    <el-button v-if="announcements.length > 1" @click="onClick" class="btn-more">
      <i :class="isActive ? 'el-icon-caret-top' : 'el-icon-caret-bottom'"></i>
      <span>{{ btnMassage }}</span>
    </el-button>
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
  data() {
    return {
      isActive: false,
      btnMassage: 'More',
    };
  },
  methods: {
    onClick() {
      if (this.isActive === false) {
        this.isActive = true;
        this.btnMassage = 'Pack up';
      } else {
        this.isActive = false;
        this.btnMassage = 'More';
      }
    },
  },
};
</script>

<style scoped>

.el-scrollbar .el-scrollbar__wrap {
  max-height: 20em;
  overflow-x:hidden;
}

.el-scrollbar__wrap .el-scrollbar__view {
  height: 100%;
}

.fade-enter-active, .fade-leave-active {
  transition: all 1s;
}
.fade-enter {
  opacity: 0;
  transform: translate(-20em, -60em);
}
.fade-leave-to {
  transform: translate(20em, 10em);
}

.fade-move {
  transition: transform 1s;
}

.course-announcement {
  display: flex;
  flex-direction: column;
  justify-content: center;
  border: 1px solid #EBEEF5;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,.1);
}

.btn-more {
  width: 100%;
  margin: 0;
  background-color: #f9fafc;
}

.btn-more:hover {
  color: #409eff;
  background-color: #f9fafc;
}

.announcements-panel-active {
  margin: 0;
  width: 100%;
  height: 20em;
  transition: height .8s;
}

.announcements-panel-close {
  margin: 0;
  width: 100%;
  height: 0em;
  transition: height .8s;
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

.announcement-card {
  margin: 1em 0;
  height: auto;
  border: 0;
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
