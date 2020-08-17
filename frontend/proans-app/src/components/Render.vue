<template>
  <div>
    <span v-html="rawHtml"></span>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor';

export default {
  name: 'Render',
  data() {
    return {
      rawHtml: '',
    };
  },
  props: {
    markdown: String,
  },
  watch: {
    markdown() {
      this.rawHtml = mavonEditor.mixins[0].data().markdownIt.render(this.markdown);
    },
  },
};
</script>

<style>
</style>
