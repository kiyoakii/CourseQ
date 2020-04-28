<template>
  <div>
    <!-- This is the Editor component. -->
    <mavon-editor v-model="value"></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'Editor',
  props: {
    value: {
      type: String,
      default: '',
    },
  },
};
</script>

<style>

</style>
