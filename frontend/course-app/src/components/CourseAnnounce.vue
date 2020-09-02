<template>
  <div class="course-announcement">
    <!-- This is CourseAnnounce view. -->
    <el-scrollbar>
      <div v-if="allinfo.announces && allinfo.announces.length > 0"
        shadow="always" class="announcement-card">
        <div class="announcement-info">
          <h3 class="announcement-title">{{ allinfo.announces[0].title }}</h3>
          <div class="announcement-publish-info">
            发布者：{{ allinfo.announces[0].author }}
          </div>
          <div class="announcement-publish-info">
            发布时间：{{ allinfo.announces[0].create_datetime }}
          </div>
        </div>
        <div class="announcement-content">
          {{ allinfo.announces[0].content }}
        </div>
      </div>
      <div v-else>
        <el-card class="box-card" shadow="hover">
        暂时还没有公告哦～
        </el-card>
      </div>
      <div v-if="allinfo.announces && allinfo.announces.length > 1"
        v-bind:class="{'announcements-panel-active': this.isActive,
        'announcements-panel-close': !this.isActive}">
        <div v-show="isActive" v-for="item in allinfo.announces.slice(1)" :key="item.title"
          shadow="always" class="announcement-card">
          <div slot="header" class="announcement-info">
            <h3 class="announcement-title">{{ item.title }}</h3>
            <div class="announcement-publish-info">
              发布者：{{ item.author }}
            </div>
            <div class="announcement-publish-info">
              发布时间：{{ item.create_datetime }}
            </div>
          </div>
          <div class="announcement-content">
            {{ item.content }}
          </div>
        </div>
      </div>
    </el-scrollbar>
    <el-button v-if="allinfo.announces && allinfo.announces.length > 1"
      @click="onClick" class="btn-more">
      <i :class="isActive ? 'el-icon-caret-top' : 'el-icon-caret-bottom'"></i>
      <span>{{ btnMassage }}</span>
    </el-button>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  props: {
    allinfo: {},
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
  border: 0px;
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
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 30px;
  width: 250px;
}

.more-announcements-header {
  font-weight:700;
  margin-left: 1em;
}

.announcement-card {
  margin: 2em 1em 0 1em;
  height: auto;
  border: 0;
  display: flex;
  flex-direction: row;
}

.announcement-title {
  margin: 0 1em;
}

.announcement-publish-info {
 font-weight:200;
 font-size: 14px;
 display: flex;
}

.announcement-content {
  display: flex;
  font-size: 1em;
  margin:0 1em;
}

</style>
