<template>
  <div>
    <search v-model="searchInfo"
    style="margin-bottom: 20px;"></search>
    <problem-list :problems="problems" :searchInfo="searchInfo"></problem-list>
  </div>
</template>

<script>
import ProblemList from '@/components/ProblemList.vue';
import Search from '@/components/Search.vue';

export default {
  name: 'SideBar',
  components: {
    ProblemList,
    Search,
  },
  data() {
    return {
      searchInfo: '',
    };
  },
  computed: {
    problems() {
      if (this.searchInfo !== '') {
        return this.$store.getters.problemsBySearch(this.searchInfo, this.$route.params.tid);
      }
      if (this.$route.params.tid === '0') {
        return this.$store.getters.problemsByLike;
      }
      if (this.$route.params.tid === 'all') {
        return this.$store.state.problems;
      }
      return this.$store.getters.problemsByTag(this.$route.params.tid);
    },
  },
};
</script>

<style scoped>

</style>
