<template>
  <el-card class="box-card">
    <!-- This is the TimeLine component. -->
    <div slot="header" class="clearfix">
      <span>版本时间轴</span>
    </div>
    <el-row class="timeline">
      <el-col :span="24" ref="wrapper" class="version_wrapper"
        :style="{ transform: 'translate(' + offset + 'px)', }"
        @mousedown.native="mouseDown" @mouseup.native="mouseUp"
        @mouseleave.native="mouseLeave">
          <el-steps align-center>
            <template v-for="(version, index) in timelineList">
              <el-step class="step"
                  :status="version.id == currentProblemId ? 'finish' : 'wait'"
                  :key="index"
                  >
                  <span slot="icon" class="circle"
                    @click.stop="changeVersion(version.id)"
                    @mousedown.stop=""
                    @mouseup.stop=""
                    v-popover="'popover' + version.id"></span>
                  <span slot="title">
                    {{ version.date.split('T')[0] }}
                  </span>
                </el-step>
            </template>
            <template v-for="(version) in timelineList">
              <el-popover
                placement="bottom"
                :key="version.id"
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
                  <el-col :span="24">
                    问题内容：{{ version.content.slice(0, 50) }}
                  </el-col>
                  <el-col :span="24">
                    修改时间：{{ version.date.split('T').join(' ') }}
                  </el-col>
                </el-row>
              </el-popover>
            </template>
          </el-steps>
      </el-col>
    </el-row>
  </el-card>
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
    this.$store.dispatch('initProblems');
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
            id: history[i].question.id,
            title: history[i].question.title,
            content: history[i].question.content,
            date: history[i].question.update_datetime,
          });
        }
      }
      res.push({
        id: problem.id,
        title: problem.title,
        content: problem.content,
        date: problem.update_datetime,
      });
      return res;
    },
    timelineList() {
      const history = this.problemHistory || [];
      return history;
    },
    // status() {
    //   return (id) => id === this.currentProblemId;
    // },
  },
  watch: {
    problemId(newVal, oldVal) {
      if (newVal !== oldVal) {
        console.log(111);
        this.currentProblemId = newVal;
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
      let min = -(this.timelineList.length * 200 - this.$refs.wrapper.$el.offsetWidth);
      min = min < 0 ? min : -9999;
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
      } else if (this.offset < min) {
        console.log('min');
        this.timer = setInterval(() => {
          const delta = this.offset - min;
          this.offset -= delta / 10 < -1 ? delta / 10 : -1;
          if (this.offset > min) {
            clearInterval(this.timer);
            this.offset = min;
          }
        }, 1000 / 60);
      } else {
        console.log('center');
        this.timer = setInterval(() => {
          const delta = -this.offset;
          this.offset += delta / 10 > 1 ? delta / 10 : 1;
          if (this.offset >= max) {
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
</style>

<style scoped>

.circle {
  width: 24px;
  height: 24px;
  display: inline-block;
  background: #f60;
}

.timeline {
  user-select: none;
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
  width: 200px;
}

.popover-content {
  flex-direction: column;
}

</style>
