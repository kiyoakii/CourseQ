<template>
  <div>
    <div style="margin-bottom: 30px;">
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">教师/助教回答</span>
        </div>
        <div v-if="teacherAnswer != null" class="text item">
          {{ teacherAnswer.content }}
        </div>
        <div v-else class="text item">
          暂时没有回答噢
        </div>
        <div class="footer">
          <div v-if="teacherAnswer != null" class="edit-info">
            <span>{{ teacherAnswer.author.nickname }} 于
              {{ (new Date(teacherAnswer.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC'}) }} 修改</span>
          </div>
          <div v-else></div>
          <div class="buttons">
            <div v-show="!teacherEditorShow">
              <el-button type="primary" icon="el-icon-edit" size="small"
                @click="teacherEditorShow = true;
                tAnswer = teacherAnswer !== null ? teacherAnswer.content:''">编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="teacherEditorShow">
          <mavon-editor v-model="tAnswer"></mavon-editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="teacherEditorShow = false"></el-button>
            <el-button type="primary" icon="el-icon-position" size="small"
              @click="handleTeacherEdit"></el-button>
          </div>
        </div>
      </el-card>
    </div>
    <div>
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">学生回答</span>
        </div>
        <div v-if="studentAnswer != null" class="text item">
          {{ studentAnswer.content }}
        </div>
        <div v-else>
          暂时没有回答噢
        </div>
        <div class="footer">
          <div v-if="studentAnswer != null" class="edit-info">
            <span>{{ studentAnswer.author.nickname }} 于
              {{ (new Date(studentAnswer.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC'}) }} 修改</span>
          </div>
          <div v-else></div>
          <div class="buttons">
            <div v-show="!studentEditorShow">
              <el-button type="primary" icon="el-icon-edit" size="small"
                @click="studentEditorShow = true;
                tAnswer = studentAnswer !== null ?studentAnswer.content:''">编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="studentEditorShow">
          <mavon-editor v-model="sAnswer"></mavon-editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="studentEditorShow = false"></el-button>
            <el-button type="primary" icon="el-icon-position" size="small"
              @click="handleStudentEdit"></el-button>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AnswerCard',
  props: {
    teacherAnswer: {
      type: Object,
    },
    studentAnswer: {
      type: Object,
    },
    problemId: Number,
  },
  data() {
    return {
      teacherEditorShow: false,
      studentEditorShow: false,
      value: '',
      tAnswer: '',
      sAnswer: '',
    };
  },
  methods: {
    handleTeacherEdit() {
      if (this.teacherAnswer !== null) {
        this.axios.put(`/api/v1/answers/${this.teacherAnswer.id}`,
          { content: this.tAnswer })
          .then((res) => {
            console.log(res);
            this.teacherEditorShow = false;
            this.$emit('updateProblem', this.problemId);
          });
      } else {
        this.axios.post(`/api/v1/questions/${this.problemId}/answers`,
          { content: this.tAnswer, is_teacher: true })
          .then((res) => {
            console.log(res);
            this.teacherEditorShow = false;
            this.$emit('updateProblem', this.problemId);
          });
      }
    },
    handleStudentEdit() {
      if (this.studentAnswer !== null) {
        this.axios.put(`/api/v1/answers/${this.studentAnswer.id}`,
          { content: this.sAnswer })
          .then((res) => {
            console.log(res);
            this.studentEditorShow = false;
            this.$emit('updateProblem', this.problemId);
          });
      } else {
        this.axios.post(`/api/v1/questions/${this.problemId}/answers`,
          { content: this.sAnswer, is_teacher: false })
          .then((res) => {
            console.log(res);
            this.studentEditorShow = false;
            this.$emit('updateProblem', this.problemId);
          });
      }
    },
  },
};
</script>

<style>
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
  margin-top: 20px;
}
.buttons {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

</style>
