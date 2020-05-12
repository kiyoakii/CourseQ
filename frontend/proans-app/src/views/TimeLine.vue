<template>
  <el-card class="box-card">
    <!-- This is the TimeLine component. -->
    <div slot="header" class="clearfix">
      <span>版本时间轴</span>
    </div>
    <ul class="timeline-list">
      <li class="timeline-item" v-for="(item, i) in timelineList" :key="i">
        <div v-if="i !== 0"
          class="timeline-item-line timeline-item-line-left"></div>
        <div v-if="i != timelineList.length - 1"
          class="timeline-item-line timeline-item-line-right"></div>
        <router-link :to="'./' + item.versionId">
          <el-tooltip class="item" effect="light" placement="top">
            <div slot="content">
              <div class="timeline-item-content">
                <span class="timeline-item-desc">
                  {{ item.userId + '进行的修改：' }}
                </span>
                <div class="timeline-item-desc">
                  {{ item.desc }}
                </div>
                <div class="timeline-item-time">{{ item.time }}</div>
              </div>
            </div>
            <div class="timeline-item-node"
              @click="chooseVersion(item.versionId)"
              :class="activeVersion === item.versionId ? 'timeline-item-node-active' : ''"></div>
          </el-tooltip>
        </router-link>
        <router-link :to="'./' + item.versionId + '/diff'">
          <el-tooltip class="item" effect="light" placement="top"
            v-if="i != timelineList.length - 1">
            <div slot="content">
              点击查看两个版本的差别
            </div>
            <i class="el-icon-document-copy"></i>
          </el-tooltip>
        </router-link>
      </li>
    </ul>
  </el-card>
</template>

<script>
export default {
  name: 'TimeLine',
  props: {
    timelineList: {
      type: Array,
      default() {
        return [
          {
            versionId: '0',
            time: '2020-04-29',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '1',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '2',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '3',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '4',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '5',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
          {
            versionId: '6',
            time: '2020-04-28',
            userId: '1234567',
            desc: '使用动态规划可以将复杂度降为O(n)',
          },
        ];
      },
    },
  },
  data() {
    return {
      activeVersion: '0',
    };
  },
  methods: {
    chooseVersion(id) {
      this.activeVersion = id;
    },
  },
};
</script>

<style scoped>

a {
  text-decoration: none;
  color: black;
}

.timeline-container {
  display: flex;
  justify-content: center;
  /* align-items: center; */
}

.timeline-list {
  display: flex;
  height: 50px;
}

.timeline-item {
  position: relative;
  display: flex;
  width: 100px;
  flex-shrink: 0;
  justify-items: baseline;
}
.timeline-item-node {
  position: absolute;
  background-color: #e4e7ed;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  top: 15px;
  left: calc(50% - 10px);
  width: 20px;
  height: 20px;
  cursor: pointer;
}
.el-icon-document-copy {
  display: none;
}
ul:hover .el-icon-document-copy {
  display: flex;
  position: absolute;
  top: 15px;
  right: -10px;
  z-index: 1;
  font-size: 16px;
  cursor: pointer;
}
.timeline-item-node-active {
  background-color: #409eff;
}

.timeline-item-line {
  position: absolute;
  width: 50%;
  top: 25px;
  border-top: 2px solid #e4e7ed;
}

.timeline-item-line-left {
  left: 0;
}

.timeline-item-line-right {
  left: 50%;
}

.timeline-item-content {
  width: 100%;
  color: black;
}

.timeline-item-desc {
  text-align: center;
  font-size: 14px;
  font-weight: 300;
}

.timeline-item-time {
  text-align: center;
  font-size: 12px;
  margin-top:10px;
  font-weight: 200;
}

</style>
