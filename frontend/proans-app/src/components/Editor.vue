<template>
  <div>
    <!-- This is the Editor component. -->
    <mavon-editor v-model="value"></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'Editor',
  data() {
    return {
      value: '',
    };
  },
};
</script>

<style>

</style>
