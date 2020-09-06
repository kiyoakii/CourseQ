<template>
  <el-row class="timeline" v-if="timelineList.length !== 1">
    <el-col :span="24">
      <el-scrollbar class="scrollbar">
        <el-steps>
          <template v-for="(version, index) in timelineList">
            <el-step class="step"
                :status="version.id == currentProblemId ? 'finish' : 'wait'"
                :key="'step' + version.id"
                >
                <span slot="icon"
                  :class="version.id === currentProblemId ? index === 0 ? 'el-icon-star-on' :
                    'circle-active' : index === 0 ? 'el-icon-star-off' : 'circle'"
                  @click.stop="changeVersion(version.id)"
                  v-popover="'popover' + version.id">
                  <el-popover
                    placement="bottom"
                    :key="'popover' + version.id"
                    :ref="'popover' + version.id"
                    width="220"
                    :close-delay="20"
                    trigger="hover"
                    >
                    <el-row type="flex" class="popover-content" justify="center"
                      >
                      <el-col :span="24">
                        问题标题：{{ version.title.slice(0, 20) }}
                      </el-col>
                      <!-- <el-col :span="24">
                        修改内容：
                        <span v-if="version.type === 0"> 问题</span>
                        <span v-if="version.type === 1"> 教师/助教回答</span>
                        <span v-if="version.type === 2"> 学生回答</span>
                      </el-col> -->
                      <el-col :span="24">
                        修改时间：{{ version.date.split('T').join(' ') }}
                      </el-col>
                    </el-row>
                  </el-popover>
                </span>
                <!-- <span slot="title">
                  {{ version.date.split('T')[0] }}
                </span> -->
              </el-step>
          </template>
        </el-steps>
      </el-scrollbar>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'TimeLine',
  props: {
    problemId: {
      type: Number,
      default: 30,
    },
  },
  data() {
    return {
      activeVersion: 0,
      offset: 0,
      oldX: 0,
      timer: 0,
      isMouseMove: false,
      isMouseDown: false,
      currentProblemId: -1,
    };
  },
  beforeCreate() {
    // this.$store.dispatch('initProblems');
  },
  beforeMount() {
    this.currentProblemId = this.problemId;
  },
  computed: {
    problemHistory() {
      const problem = this.$store.getters.problem(this.problemId);
      if (!problem) {
        return [];
      }
      const res = [];
      const history = [...problem.history];
      for (let i = 0; i < history.length; i += 1) {
        if (history[i].question) {
          res.push({
            id: history[i].id,
            title: history[i].question.title,
            content: history[i].question.content,
            date: history[i].modify_time,
          });
        }
      }
      res.push({
        id: problem.id,
        title: problem.title,
        content: problem.content,
        date: problem.create_datetime,
      });
      return res;
    },
    timelineList() {
      const history = this.problemHistory || [];
      return history.reverse();
    },
  },
  watch: {
    problemId(newVal, oldVal) {
      if (newVal !== oldVal) {
        this.currentProblemId = newVal;
        this.$forceUpdate();
      }
    },
  },
  methods: {
    changeVersion(id) {
      this.currentProblemId = id;
      this.$emit('changeversion', { id });
    },
    mouseMove(ev) {
      this.isMouseMove = true;
      this.offset += ev.clientX - this.oldX;
      this.oldX = ev.clientX;
    },
    mouseDown(ev) {
      this.isMouseDown = true;
      this.oldX = ev.clientX;
      this.$refs.wrapper.$el.onmousemove = this.mouseMove;
    },
    mouseLeave(ev) {
      if (this.isMouseMove && this.isMouseDown) {
        this.mouseUp(ev);
      }
    },
    mouseUp(ev) {
      if (!this.isMouseMove || !this.isMouseDown) {
        return;
      }
      this.isMouseMove = false;
      this.isMouseDown = false;
      this.offset += ev.clientX - this.oldX;
      this.oldX = ev.clientX;
      this.$refs.wrapper.$el.onmousemove = null;
      const max = 0;
      const min = -(this.timelineList.length * 200 - this.$refs.wrapper.$el.offsetWidth);
      console.log('up');
      if (this.offset > max) {
        console.log('max');
        this.timer = setInterval(() => {
          const delta = this.offset - max;
          this.offset -= delta / 10 > 1 ? delta / 10 : 1;
          if (this.offset <= max) {
            clearInterval(this.timer);
            this.offset = 0;
          }
        }, 1000 / 60);
      } else if (this.offset < min && min < 0) {
        console.log('min');
        this.timer = setInterval(() => {
          const delta = this.offset - min;
          this.offset -= delta / 10 < -1 ? delta / 10 : -1;
          if (this.offset > min) {
            clearInterval(this.timer);
            this.offset = min;
          }
        }, 1000 / 60);
      } else if (min >= 0) {
        console.log('center');
        this.timer = setInterval(() => {
          const delta = this.offset;
          this.offset -= delta / 10 < 1 ? delta / 10 : -1;
          if (this.offset > 0) {
            clearInterval(this.timer);
            this.offset = 0;
          }
        }, 1000 / 60);
      }
    },
  },
};
</script>

<style>

.el-step__icon {
  border: none !important;
  cursor: pointer;
  width: auto;
}

.el-step__icon:hover .circle{
  background: #68b4ff !important;
}

.is-wait .el-step__icon .circle {
  border-radius: 50%;
  border: none;
  background: #C0C4CC;
}

.is-finish .el-step__icon .circle {
  border-radius: 50%;
  border: none;
  background: #409EFF;
}

.el-step__icon-inner {
  display: none !important;
}

.is-finish {
  color: #409EFF !important;
  border-color: #409EFF !important;
}

.is-process {
  color: #409EFF !important;
  border-color: #409EFF !important;
}

.timeline .el-scrollbar__wrap {
  overflow-x: hidden;
  display: flex;
  align-items: center;
}
</style>

<style scoped>

.el-icon-star-on, .el-icon-star-off {
  font-size: 26px;
  user-select: none;
  outline:none;
}

.el-icon-star-off {
  font-size: 22px;
  outline: none;
}

.el-icon-star-off:hover:before {
  color: #409EFF;
  content: "\e797";
}

.scrollbar {
  height: 40px;
}

.circle {
  width: 16px;
  height: 16px;
  display: inline-block;
  background: #f60;
  outline: none;
}

.circle-active {
  width: 16px;
  height: 16px;
  display: inline-block;
  background: #409EFF;
  outline: none;
  border-radius: 50%;
}

.timeline {
  user-select: none;
  margin-bottom: 20px !important;
}

.version {
  width: 200px;
  height: 200px;
  border: 1px solid #eeddee;
  white-space: normal;
  border-radius: 5px;
  display: inline-block;
  margin-right: 10px;
  flex-shrink: 0;
}

.version_wrapper {
  white-space: nowrap;
  display: flex;
}

.step {
  width: 100px;
  flex-shrink: 0;
  flex-basis: 100px !important;
}

.popover-content {
  flex-direction: column;
}

</style>
