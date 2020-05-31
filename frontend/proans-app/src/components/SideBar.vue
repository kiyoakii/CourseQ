<template>
  <div>
    <search></search>
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
    };
  },
  mounted() {
    this.axios.get('/v1/proans/problems?id=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.problems = res.data.data.problems;
      });
  },
};
</script>

<style>

</style>
