<template>
  <div>
    <el-container>
      <el-aside>
        <problem-list></problem-list>
      </el-aside>
      <el-main>
        <editor></editor>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Editor from '@/components/Editor.vue';
import ProblemList from '@/components/ProblemList.vue';

export default {
  name: 'VueContent',
  components: {
    Editor,
    ProblemList,
  },
};
</script>

<style>

</style>
