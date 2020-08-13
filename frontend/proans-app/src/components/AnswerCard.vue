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
          <div v-if="teacherAnswer != null" class="edit-info">
            <span>{{ teacherAnswer.author.nickname }} 于
              {{ teacherAnswer.update_datetime }} 修改</span>
          </div>
          <div v-else></div>
          <div class="buttons">
            <el-button size="medium">编辑</el-button>
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
              {{ studentAnswer.update_datetime }} 修改</span>
          </div>
          <div v-else></div>
          <div class="buttons">
            <el-button size="medium">编辑</el-button>
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
</style>
