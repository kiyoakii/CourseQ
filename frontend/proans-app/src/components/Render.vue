<template>
  <div>
    <span class="markdown-body" v-html="rawHtml" :class="(transfer) ?
      'markdown-limit-height' : ''"></span>
  </div>
</template>

<script>
import { mavonEditor } from 'mavon-editor';

export default {
  name: 'Render',
  props: {
    markdown: String,
    transfer: Boolean,
  },
  methods: {
    nodeFilter(value) {
      const regImg = new RegExp('.*!\\[.*]\\(.*\\)', 'gm');
      value = value.replace(regImg, '「图片」');
      const regCode = new RegExp('```([\\s\\S]*?)```[\\s]?', 'gm');
      value = value.replace(regCode, '「代码」');
      const regLink = new RegExp('\\[[\\s\\S]*?\\]\\([\\s\\S]*?\\)', 'gm');
      value = value.replace(regLink, '「链接」');
      const regSpaceLine = new RegExp('^((\\r\\n)|(\\n))', 'gm');
      value = value.replace(regSpaceLine, '');
      const regTitle = new RegExp('^(#+)(.*)', 'gm');
      value = value.replace(regTitle, '$2');
      const regBold = new RegExp('(\\*\\*|__)(.*?)\\1', 'gm');
      value = value.replace(regBold, '$2');
      const regHighlight = new RegExp('(\\=\\=|__)(.*?)\\1', 'gm');
      value = value.replace(regHighlight, '$2');
      // const regItalic = new RegExp('(\\*|_)(.*?)\\1');
      // value = value.replace(regItalic, '$3');
      const regDelete = new RegExp('\\~\\~(.*?)\\~\\~', 'gm');
      value = value.replace(regDelete, '$1');
      const regQuote = new RegExp('^(\\> )(.*)', 'gm');
      value = value.replace(regQuote, '$2');
      const regDisorder = new RegExp('^[\\s]*[-\\*\\+] +(.*)', 'gm');
      value = value.replace(regDisorder, '$1');
      const regOrder = new RegExp('^[\\s]*[0-9]+\\.(.*)', 'gm');
      value = value.replace(regOrder, '$1');
      console.log(value);
      return value;
    },
  },
  computed: {
    rawHtml() {
      let returnResult;
      console.log(this.transfer);
      if (this.transfer) {
        const value = this.nodeFilter(this.markdown);
        const renderResult = mavonEditor.getMarkdownIt().render(value);
        console.log(renderResult);
        const regTable = new RegExp('\\<table.*?\\>[\\s\\S]*?\\<\\/table\\>');
        returnResult = renderResult.replace(regTable, '「表格」');
      } else {
        returnResult = mavonEditor.getMarkdownIt().render(this.markdown);
      }
      return returnResult;
    },
  },
};
</script>

<style scoped>
.markdown-limit-height {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 4;
  overflow: hidden;
}
</style>
