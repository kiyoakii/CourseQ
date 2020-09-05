<template>
  <div>
    <div style="margin-bottom: 30px;">
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">教师/助教回答</span>
        </div>
        <div v-if="!teacherEditorShow">
          <div v-if="teacherAnswer != null" class="text item">
            <render :markdown="teacherAnswer.content"></render>
          </div>
          <div v-else class="text item">
            暂时没有回答噢
          </div>
        </div>
        <div class="footer">
          <div v-if="teacherAnswer && !teacherEditorShow" class="edit-info">
            <span>{{ teacherAnswer.author.nickname }} 于
              {{ (new Date(teacherAnswer.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC', hour12: false}) }} 修改</span>
          </div>
          <div class="buttons">
            <div v-show="!teacherEditorShow">
              <el-button type="primary" icon="el-icon-edit" size="small"
                @click="handleTeacherClick"
                :disabled="disableInteract || !isTeacherOrAssistant"
                plain>编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="teacherEditorShow">
          <editor v-model="tAnswer"></editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="closeTeacherEdit" plain>取消</el-button>
            <el-button type="primary" icon="el-icon-position" size="small"
              @click="handleTeacherEdit" plain>确认</el-button>
          </div>
        </div>
      </el-card>
    </div>
    <div>
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">学生回答</span>
        </div>
        <div v-if="!studentEditorShow">
          <div v-if="studentAnswer" class="text item">
            <render :markdown="studentAnswer.content"></render>
          </div>
          <div v-else>
            暂时没有回答噢
          </div>
        </div>
        <div class="footer">
          <div v-if="studentAnswer != null && !studentEditorShow" class="edit-info">
            <span>{{ studentAnswer.author.nickname }} 于
              {{ (new Date(studentAnswer.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC', hour12: false}) }} 修改</span>
          </div>
          <div class="buttons">
            <div v-show="!studentEditorShow">
              <el-button type="primary" icon="el-icon-edit" size="small"
                @click="handleStudentClick"
                :disabled="disableInteract || !isStudent"
                plain>编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="studentEditorShow">
          <editor v-model="sAnswer"></editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="closeStudentEdit" plain>取消</el-button>
            <el-button type="primary" icon="el-icon-position" size="small"
              @click="handleStudentEdit" plain>确认</el-button>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
import Render from '@/components/Render.vue';
import Editor from './Editor.vue';
import { instance } from '../helpers/instances';

export default {
  name: 'AnswerCard',
  components: {
    Render,
    Editor,
  },
  props: {
    teacherAnswer: {
      type: Object,
    },
    studentAnswer: {
      type: Object,
    },
    problemId: Number,
    disableInteract: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      teacherEditorShow: false,
      studentEditorShow: false,
      value: '',
      tAnswer: '',
      sAnswer: '',
      lockTimer: 0,
      lockTimes: 0,
    };
  },
  computed: {
    isTeacherOrAssistant() {
      return this.$store.state.auth === '教师'
        || this.$store.state.auth === '助教';
    },
    isStudent() {
      return this.$store.state.auth === '学生';
    },
  },
  methods: {
    startTimer() {
      if (this.lockTimer) {
        window.clearInterval(this.lockTimer);
      }
      this.lockTimer = setInterval(() => {
        this.axios({
          method: 'POST',
          url: `/api/v1/questions/${this.$route.params.qid}/lock`,
        }).then((res) => {
          this.lockTimes += 1;
          if (this.lockTimes > 40) {
            this.$message.info('由于长时间未改动，你即将退出编辑界面.');
            clearInterval(this.lockTimer);
            this.axios.post(`/v1/questions/${this.$route.params.qid}/unlock`)
              .then(() => {
                this.$router.push({
                  name: 'ProblemView',
                  params: {
                    cid: this.$route.params.cid,
                    tid: this.$route.params.tid,
                    qid: this.$route.params.qid,
                  },
                });
              });
            return;
          }
          if (res.status === 403) {
            this.$message.info('对不起，该问题已被其他用户编辑，请等待.');
            clearInterval(this.lockTimer);
            this.$nextTick(() => {
              this.$router.push({
                name: 'ProblemView',
                params: {
                  cid: this.$route.params.cid,
                  tid: this.$route.params.tid,
                  qid: this.$route.params.qid,
                },
              });
            });
          }
        });
      }, 1000 * 15);
      this.$store.state.lockTimer = this.lockTimer;
    },
    handleTeacherClick() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/lock`,
      }).then(() => {
        this.teacherEditorShow = true;
        this.tAnswer = this.teacherAnswer !== null ? this.teacherAnswer.content : '';
        this.startTimer();
      });
    },
    handleStudentClick() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/lock`,
      }).then(() => {
        this.studentEditorShow = true;
        this.sAnswer = this.studentAnswer !== null ? this.studentAnswer.content : '';
        this.startTimer();
      });
    },
    handleTeacherEdit() {
      window.clearInterval(this.lockTimer);
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/unlock`,
      }).then(() => {
        window.clearInterval(this.lockTimer);
        if (this.teacherAnswer !== null) {
          instance.put(`/api/v1/answers/${this.teacherAnswer.id}`,
            { content: this.tAnswer })
            .then(() => {
              this.teacherEditorShow = false;
              this.$emit('updateProblem', this.problemId);
            });
        } else {
          instance.post(`/api/v1/questions/${this.problemId}/answers`,
            { content: this.tAnswer, is_teacher: true })
            .then(() => {
              this.teacherEditorShow = false;
              this.$emit('updateProblem', this.problemId);
            });
        }
      });
    },
    handleStudentEdit() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/unlock`,
      }).then(() => {
        window.clearInterval(this.lockTimer);
        if (this.studentAnswer !== null) {
          instance.put(`/api/v1/answers/${this.studentAnswer.id}`,
            { content: this.sAnswer })
            .then(() => {
              this.studentEditorShow = false;
              this.$emit('updateProblem', this.problemId);
            });
        } else {
          instance.post(`/api/v1/questions/${this.problemId}/answers`,
            { content: this.sAnswer, is_teacher: false })
            .then(() => {
              this.studentEditorShow = false;
              this.$emit('updateProblem', this.problemId);
            });
        }
      });
    },
    closeTeacherEdit() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/unlock`,
      }).then(() => {
        this.teacherEditorShow = false;
        window.clearInterval(this.lockTimer);
      });
    },
    closeStudentEdit() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/unlock`,
      }).then(() => {
        this.studentEditorShow = false;
        window.clearInterval(this.lockTimer);
      });
    },
  },
};
</script>

<style scoped>
.tags {
  margin-left: 10px;
}
.el-tag {
  font-size: 10px;
}
.title {
  font-size: 18px;
}
.footer {
  padding-top: 20px;
  display: flex;
  justify-content:space-between;
  align-items: flex-end;
}
.edit-info {
  font-size: 12px;
  color: #606266;
}
.editor {
  margin-top: 0px;
}
.buttons {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

</style>
