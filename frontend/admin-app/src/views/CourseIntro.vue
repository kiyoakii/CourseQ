<template>
  <div class="intro">
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{courseName}}</span>
        <div class="footer">
          {{courseTerm}}
        </div>
      </div>
      <div class="text item">
        {{ courseIntroduction }}
      </div>
    </el-card>
    <el-card class="message-card">
      <el-row>
        <div class="text item">
          <span class="subtitle">教师信息：</span>
          <span>{{courseTutor}}</span>
        </div>
      </el-row>
      <el-row>
        <div class="text item">
          <span class="subtitle">上课时间：</span>
          <span>{{courseTime}}</span>
        </div>
      </el-row>
      <el-row>
        <div class="text item">
          <span class="subtitle">参考教材：</span>
          <span>{{courseReference}}</span>
        </div>
      </el-row>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'CourseIntro',
  data() {
    return {
      courseName: '人工智能导论',
      courseTerm: '2020 Spring',
      courseIntroduction: `人工智能是一个庞杂的学科体系，从概念上讲，
                          一切为复制生物智能而做出的努力都可纳入其中。
                          如何能够系统、全面、简洁地描述人工智能的全貌而不显得凌乱，
                          绝非易事。主要教授如何选购扫地机器人`,
      courseTutor: 'Jianmin Ji',
      courseTime: '15:55-17:30 Monday, 9:45-11:20 Wednesday',
      courseReference: '周志华 《西瓜书》',
    };
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
  font-size: 30px;
}
.subtitle {
  font-size: 22px;
}
.footer {
  padding-top: 20px;
  display: flex;
  justify-content: flex-end;
}
.intro {
  margin:0 auto;
  width:700px;
}
.message-card {
  margin-top: 50px;
}
</style>
