<template>
  <el-row class="header">
    <el-col :span="20">
      <problem-categories @click="setLike(false)"></problem-categories>
    </el-col>
    <el-col :span="4">
      <el-row type="flex" justify="space-around">
        <el-button @click="setLike(true)">我的点赞</el-button>
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
      </el-row>
    </el-col>
  </el-row>
</template>

<script>
import ProblemCategories from '@/components/ProblemCategories.vue';

export default {
  name: 'VueHeader',
  components: {
    ProblemCategories,
  },
  methods: {
    setLike(like) {
      this.$store.commit({
        type: 'setClickLike',
        like,
      });
    },
  },
};
</script>

<style scoped>
.header {
  margin: 10px 0;
}
</style>
