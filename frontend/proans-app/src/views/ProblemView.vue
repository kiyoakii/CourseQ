<template>
  <div>
    <problem-card></problem-card>
    <answer-card></answer-card>
    <discussion></discussion>
  </div>
</template>

<script>
import ProblemCard from '@/components/ProblemCard.vue';
import AnswerCard from '@/components/AnswerCard.vue';
import Discussion from '@/components/Discussion.vue';

export default {
  name: 'ProblemView',
  components: {
    ProblemCard,
    AnswerCard,
    Discussion,
  },
};
</script>

<style>

</style>
