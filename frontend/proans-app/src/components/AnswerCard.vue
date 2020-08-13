<template>
  <div>
    <div>
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
          <el-button size="medium">历史版本</el-button>
          <el-button size="medium">点赞</el-button>
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
          <el-button size="medium">历史版本</el-button>
          <el-button size="medium">编辑</el-button>
          <el-button size="medium">点赞</el-button>
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
  justify-content: flex-end;
}
</style>
