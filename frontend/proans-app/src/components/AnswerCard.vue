<template>
  <div>
    <div>
      <el-card class="box-card" shadow="hover">
        <div slot="header" class="clearfix">
          <span class="title">教师/助教回答</span>
        </div>
        <div class="text item">
          {{ teacherAnswer.content }}
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
        <div class="text item">
          {{ studentAnswer.content }}
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
  data() {
    return {
      teacherAnswer: {},
      studentAnswer: {},
    };
  },
  mounted() {
    this.axios.get('/v1/proans/answer/teacher?id=1&problem=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.teacherAnswer = res.data.data.answer;
      });
    this.axios.get('/v1/proans/answer/student?id=1&problem=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.studentAnswer = res.data.data.answer;
      });
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
