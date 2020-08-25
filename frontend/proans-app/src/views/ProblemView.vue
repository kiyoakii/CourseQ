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
      :disableInteract="disableInteract"
      @updateProblem="handleUpdateProblem"></answer-card>
    <discussion :commentList="commentList"
      :disableInteract="disableInteract"
      ></discussion>
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
        return item.id === this.versionId;
      });
      return {
        ...res.question,
        student_answer: res.student_answer,
        teacher_answer: res.teacher_answer,
        stars: problem.stars,
        liked: problem.liked,
        tags: problem.tags,
      };
    },
    problemId() {
      return this.$store.state.qid;
    },
    disableInteract() {
      return !this.problem.history;
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
    handleUpdateProblem(id) {
      this.$store.dispatch('updateProblem', { id });
    },
    updateData() {
      this.$store.dispatch('setCommentList');
      this.$store.dispatch('initProblems');
    },
    changeVersion({ id }) {
      this.versionId = id;
    },
    initStore() {
      this.$store.commit({
        type: 'setCid',
        id: Number(this.$route.params.cid),
      });
      this.$store.commit({
        type: 'setQid',
        id: Number(this.$route.params.qid),
      });
    },
  },
  beforeRouteUpdate(from, to, next) {
    next();
    this.versionId = -1;
    this.initStore();
    this.$store.dispatch('setCommentList');
  },
  mounted() {
    this.$store.dispatch('initProblems');
    this.initStore();
    this.$store.dispatch('setCommentList');
  },
};
</script>

<style scoped>
#problem > * {
  margin-bottom: 30px;
}
</style>
