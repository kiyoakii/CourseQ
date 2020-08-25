<template>
  <div>
    <div style="margin-bottom: 30px;">
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">教师/助教回答</span>
        </div>
        <div v-if="teacherAnswer != null" class="text item">
          <render :markdown="teacherAnswer.content"></render>
        </div>
        <div v-else class="text item">
          暂时没有回答噢
        </div>
        <div class="footer">
          <div v-if="teacherAnswer" class="edit-info">
            <span>{{ teacherAnswer.author.nickname }} 于
              {{ (new Date(teacherAnswer.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC'}) }} 修改</span>
          </div>
          <div v-else></div>
          <div class="buttons">
            <div v-show="!teacherEditorShow">
              <el-button type="primary" icon="el-icon-edit" size="small"
                @click="teacherEditorShow = true;
                tAnswer = teacherAnswer !== null ? teacherAnswer.content:''"
                :disabled="disableInteract"
                plain>编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="teacherEditorShow">
          <editor v-model="tAnswer"></editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="teacherEditorShow = false" plain>取消</el-button>
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
        <div v-if="studentAnswer" class="text item">
          <render :markdown="studentAnswer.content"></render>
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
                sAnswer = studentAnswer !== null ?studentAnswer.content:''"
                :disabled="disableInteract"
                plain>编辑</el-button>
            </div>
          </div>
        </div>
        <div class="editor" v-show="studentEditorShow">
          <editor v-model="sAnswer"></editor>
          <div class="buttons">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="studentEditorShow = false" plain>取消</el-button>
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
    };
  },
  methods: {
    handleTeacherEdit() {
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
    },
    handleStudentEdit() {
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
  margin-top: 20px;
}
.buttons {
  display: flex;
  justify-content: flex-end;
  margin-top: 10px;
}

</style>
