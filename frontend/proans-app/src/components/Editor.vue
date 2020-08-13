<template>
  <div>
    <div class="title">
      <el-input placeholder="主题"></el-input>
    </div>
    <mavon-editor @change="onChange" v-model="content"></mavon-editor>
    <div class="footer">
      <el-button type="primary" icon="el-icon-position" size="small">提交</el-button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Editor',
  model: {
    prop: 'content',
    event: 'submit',
  },
  props: {
  },
  methods: {
    onChange() {
      console.log(this.content);
    },
  },
};
</script>

<style scoped>
.title {

}
.footer {
  display: flex;
  justify-content: flex-end;

}
</style>>
