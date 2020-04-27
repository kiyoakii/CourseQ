<template>
  <div>
    <el-container>
      <el-aside>
        <search></search>
        <problem-list></problem-list>
      </el-aside>
      <el-main>
        <problem-card></problem-card>
        <answer-card></answer-card>
        <discussion></discussion>
        <time-line></time-line>
        <editor></editor>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import Editor from '@/components/Editor.vue';
import ProblemList from '@/components/ProblemList.vue';
import Search from '@/components/Search.vue';
import TimeLine from '@/components/TimeLine.vue';
import ProblemCard from '@/components/ProblemCard.vue';
import AnswerCard from '@/components/AnswerCard.vue';
import Discussion from '@/components/Discussion.vue';

export default {
  name: 'VueContent',
  components: {
    Editor,
    ProblemList,
    Search,
    TimeLine,
    ProblemCard,
    AnswerCard,
    Discussion,
  },
};
</script>

<style>

</style>
