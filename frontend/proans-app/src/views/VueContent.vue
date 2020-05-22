<template>
  <div>
    <el-container>
      <el-aside>
        <search></search>
        <problem-list></problem-list>
      </el-aside>
      <el-main>
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import ProblemList from '@/components/ProblemList.vue';
import Search from '@/components/Search.vue';

export default {
  name: 'VueContent',
  components: {
    ProblemList,
    Search,
  },
};
</script>

<style>

</style>
