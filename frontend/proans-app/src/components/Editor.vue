<template>
  <div>
    <mavon-editor @change="change" v-model="contentCopy" :toolbars="toolbars"
      :boxShadow="false" :tabSize="4" ref=md @imgAdd="$imgAdd"></mavon-editor>
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
        strikethrough: true, // 中划线
        mark: true, // 标记
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
        help: true, // 帮助
        undo: true, // 上一步
        redo: true, // 下一步
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
    $imgAdd(pos, $file) {
      // 第一步.将图片上传到服务器.
      const formdata = new FormData();
      formdata.append('file', $file);
      this.axios({
        url: '/api/v1/photos',
        method: 'post',
        data: formdata,
        headers: { 'Content-Type': 'multipart/form-data' },
      }).then((res) => {
        // 第二步.将返回的url替换到文本原位置![...](0) -> ![...](url)
        /**
        * $vm 指为mavonEditor实例，可以通过如下两种方式获取
        * 1. 通过引入对象获取: `import {mavonEditor} from ...` 等方式引入后，`$vm`为`mavonEditor`
        * 2. 通过$refs获取: html声明ref : `<mavon-editor ref=md ></mavon-editor>，`$vm`为 `this.$refs.md`
        */
        // console.log(res);
        this.$refs.md.$img2Url(pos, res.data.url);
      });
    },
  },
  watch: {
    content() {
      this.contentCopy = this.content;
    },
  },
};
</script>

<style scoped>
.footer {
  display: flex;
  justify-content: flex-end;
}
</style>>
