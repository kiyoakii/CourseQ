<template>
  <div>
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{ problem.title }}</span>
        <span class="tags" v-for="tag in problem.tags" :key="tag">
          <el-tag class="success" size="mini">{{ tag }}</el-tag>
        </span>
      </div>
      <div class="text item">
        {{ problem.content }}
      </div>
      <div class="footer">
        <el-button size="medium">历史版本</el-button>
        <el-button size="medium">编辑</el-button>
        <el-button size="medium">点赞</el-button>
        <el-button size="medium">关注</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'ProblemCard',
  data() {
    return {
      problem: {},
    };
  },
  mounted() {
    this.axios.get('/v1/proans/problem/detail?id=1&problem=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.problem = res.data.data.problem;
      });
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
  justify-content: flex-end;
}
</style>
