<template>
  <div class="editor">
    <mavon-editor @change="change" v-model="contentCopy" :toolbars="toolbars"
      :boxShadow="false" :tabSize="4" style="border: 1px solid #EBEEF5;"></mavon-editor>
  </div>
</template>

<script>
export default {
  name: 'Editor',
  data() {
    return {
      toolbars: {
        bold: true, // 粗体
        italic: true, // 斜体
        header: true, // 标题
        underline: true, // 下划线
        // strikethrough: true, // 中划线
        // mark: true, // 标记
        superscript: true, // 上角标
        subscript: true, // 下角标
        quote: true, // 引用
        ol: true, // 有序列表
        ul: true, // 无序列表
        link: true, // 链接
        imagelink: true, // 图片链接
        code: true, // code
        table: true, // 表格
        fullscreen: true, // 全屏编辑
        // help: true, // 帮助
        // undo: true, // 上一步
        // redo: true, // 下一步
        subfield: true, // 单双栏模式
        preview: true, // 预览
      },
      contentCopy: '',
    };
  },
  props: {
    content: String,
  },
  model: {
    prop: 'content',
    event: 'change',
  },
  methods: {
    change(val) {
      this.$emit('change', val);
    },
  },
  watch: {
    content() {
      this.contentCopy = this.content;
    },
  },
};
</script>

<style>

.editor .v-note-show .v-show-content.scroll-style.scroll-style-border-radius {
  background-color: #fefefe !important;
}

</style>

<style scoped>
.footer {
  display: flex;
  justify-content: flex-end;
}
</style>>
