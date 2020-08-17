<template>
  <div id="problem">
    <time-line
      :problemId="problemId"
      @changeversion="changeVersion"
      >
    </time-line>
    <problem-card :problem="problem"
      @updateProblem="handleUpdateProblem"></problem-card>
    <answer-card :studentAnswer="studentAnswer"
      :teacherAnswer="teacherAnswer"
      :problemId="problemId"
      @updateProblem="handleUpdateProblem"></answer-card>
    <discussion :commentList="commentList"></discussion>
  </div>
</template>

<script>
import ProblemCard from '@/components/ProblemCard.vue';
import AnswerCard from '@/components/AnswerCard.vue';
import Discussion from '@/components/Discussion.vue';
import TimeLine from '../components/TimeLine.vue';

export default {
  name: 'ProblemView',
  components: {
    ProblemCard,
    AnswerCard,
    Discussion,
    TimeLine,
  },
  data() {
    return {
      versionId: -1,
    };
  },
  computed: {
    problem() {
      const problem = this.$store.getters.problem(this.$store.state.qid);
      if (this.versionId === -1) {
        return problem;
      }
      if (!problem) {
        return null;
      }
      if (this.versionId === problem.id) {
        return problem;
      }
      console.log(problem);
      const res = problem.history.find((item) => {
        console.log(item.question && item.question.id, this.versionId);
        return item.question && (item.question.id === this.versionId);
      });
      return {
        ...res.question,
        student_answer: res.student_answer,
        teacher_answer: res.teacher_answer,
      };
    },
    problemId() {
      return this.$store.state.qid;
    },
    studentAnswer() {
      return this.problem && this.problem.student_answer ? this.problem.student_answer : null;
    },
    teacherAnswer() {
      return this.problem && this.problem.teacher_answer ? this.problem.teacher_answer : null;
    },
    commentList() {
      return this.$store.getters.commentList || [];
    },
  },
  methods: {
    handleUpdateProblem() {
      this.$store.commit('updateProblem', this.problem);
    },
    updateData() {
    },
    changeVersion({ id }) {
      this.versionId = id;
    },
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to, from);
    next();
    this.versionId = -1;
    this.$store.commit({
      type: 'setQid',
      id: this.$route.query.qid,
    });
  },
  beforeUpdate() {
    this.$store.commit({
      type: 'setQid',
      id: this.$route.query.qid,
    });
  },
  beforeCreate() {
    this.$store.commit({
      type: 'setQid',
      id: this.$route.query.qid,
    });
    this.$store.dispatch('setCommentList');
  },
};
</script>

<style>
#problem > * {
  margin-bottom: 30px;
}
</style>
