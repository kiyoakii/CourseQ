<template>
  <div>
    <problem-card :problem="problem"
      @updateProblem="handleUpdateProblem"></problem-card>
    <answer-card :studentAnswer="studentAnswer"
      :teacherAnswer="teacherAnswer"
      :problemId="problem.id"
      @updateProblem="handleUpdateProblem"></answer-card>
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
  methods: {
    handleUpdateProblem(qid) {
      this.$store.commit('updateProblem', this.problem);
      setTimeout(() => {
        this.problem = this.$store.getters.problem(qid);
        this.studentAnswer = this.problem.student_answer;
        this.teacherAnswer = this.problem.teacher_answer;
      }, 400);
    },
    updateData() {
      console.log(this.$route.query.qid);
      setTimeout(() => {
        this.problem = this.$store.getters.problem(this.$route.query.qid);
        this.studentAnswer = this.problem.student_answer;
        this.teacherAnswer = this.problem.teacher_answer;
      }, 400);
      this.axios.get(`/api/v1/questions/${this.$route.query.qid}/discussions`)
        .then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
            return;
          }
          this.commentList = res.data;
        });
    },
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to, from);
    next();
    if (this.$route.query.qid !== undefined) {
      this.updateData();
    }
  },
  beforeMount() {
    if (this.$route.query.qid !== undefined) {
      this.updateData();
    }
  },
};
</script>

<style>

</style>
