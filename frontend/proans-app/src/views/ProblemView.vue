<template>
  <div>
    <problem-card :problem="problem"></problem-card>
    <answer-card :studentAnswer="studentAnswer"
      :teacherAnswer="teacherAnswer"></answer-card>
    <discussion :commentList="commentList"></discussion>
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
      commentList: [],
    };
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to, from);
    next();
    if (this.$route.query.qid !== undefined) {
      console.log(this.$route.query.qid);
      this.problem = this.$store.getters.problem(this.$route.query.qid);
      this.studentAnswer = this.problem.student_answer;
      this.teacherAnswer = this.problem.teacher_answer;
      this.axios.get(`/api/v1/questions/${this.$route.query.qid}/discussions`)
        .then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
            return;
          }
          this.commentList = res.data;
        });
    }
  },
};
</script>

<style>

</style>
