<template>
  <div>
    <search></search>
    <problem-list></problem-list>
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
};
</script>

<style>

</style>
