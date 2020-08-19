<template>
  <div>
    <search v-model="searchInfo"
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
  computed: {
    problems() {
      if (this.searchInfo !== '') {
        return this.$store.getters.problemsBySearch(this.searchInfo);
      }
      return this.$store.getters.problemsByTag(this.$route.params.tid);
    },
  },
};
</script>

<style>

</style>
