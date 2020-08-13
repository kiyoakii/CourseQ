<template>
  <div>
    <problem-card :problem="problem"></problem-card>
    <answer-card :studentAnswer="studentAnswer"
      :teacherAnswer="teacherAnswer"></answer-card>
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
  data() {
    return {
      problem: {},
      studentAnswer: {},
      teacherAnswer: {},
    };
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to, from);
    next();
    if (this.$route.query.pid !== undefined) {
      console.log(this.$route.query.pid);
      this.problem = this.$store.getters.problem(this.$route.query.pid);
      this.studentAnswer = this.problem.student_answer;
      this.teacherAnswer = this.problem.teacher_answer;
    }
  },
};
</script>

<style>

</style>
