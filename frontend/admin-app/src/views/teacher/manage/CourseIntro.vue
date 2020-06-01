<template>
  <div class="intro">
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{ allInfo.name }}</span>
        <div class="footer">
          {{courseTerm}}
        </div>
      </div>
      <div class="text item">
        {{ allInfo.intro }}
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
  props: {
    allInfo: {},
  },
  data() {
    return {
      courseTerm: '2020 Spring',
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
