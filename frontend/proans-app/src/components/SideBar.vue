<template>
  <div>
    <search :tags="tags"
    v-model="searchInfo"></search>
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
      problems: [],
      tags: [],
      searchInfo: '',
    };
  },
  beforeRouteUpdate(to, from, next) {
    console.log(to, from);
    next();
    this.problems = this.$store.getters.problemsByTag(this.$route.query.tid);
  },
  watch: {
    searchInfo(newInfo) {
      this.problems = this.$store.getters.problemsBySearch(newInfo);
    },
  },
  mounted() {
    const self = this;
    setTimeout(() => {
      this.tags = self.$store.getters.allTags;
    }, 2000);
  },
};
</script>

<style>

</style>
