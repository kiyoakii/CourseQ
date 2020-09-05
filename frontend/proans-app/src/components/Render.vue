<template>
  <div>
    <span class="markdown-body" v-html="rawHtml"></span>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor';

export default {
  name: 'Render',
  props: {
    markdown: String,
  },
  computed: {
    rawHtml() {
      return mavonEditor.getMarkdownIt().render(this.markdown);
    },
  },
};
</script>

<style scoped>
.markdown-body {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
