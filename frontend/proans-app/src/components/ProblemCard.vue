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
        {{ problem.desc }}
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
      problem: {
        title: '动态规划',
        tags: ['标签一', '标签二', '标签三'],
        desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
               规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
      },
    };
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
