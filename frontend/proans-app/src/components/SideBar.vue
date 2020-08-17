<template>
  <div>
    <search :tags="tags"
    v-model="searchInfo"
    style="margin-bottom: 20px;"></search>
    <problem-list :problems="problems"></problem-list>
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
  watch: {
    searchInfo(newInfo) {
      this.problems = this.$store.getters.problemsBySearch(newInfo);
    },
  },
  computed: {
    tags() {
      return this.$store.getters.allTags;
    },
    problems() {
      return this.$store.getters.problemsByTag(this.$route.params.tid);
    },
  },
};
</script>

<style>

</style>
