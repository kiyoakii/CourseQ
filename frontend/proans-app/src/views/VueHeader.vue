<template>
  <div>
    This is VueHeader view.
    <problem-categories></problem-categories>
  </div>
</template>

<script>
import ProblemCategories from '../components/ProblemCategories.vue';

export default {
  name: 'VueHeader',
  components: {
    ProblemCategories,
  },
};
</script>

<style>

</style>
