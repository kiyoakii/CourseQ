<template>
  <div>
    <el-card class="comment">
      <div class="comment-header">
        <el-row type="flex" justify="space-between">
          <div class="comment-user">新的讨论</div>
        </el-row>
      </div>
      <div class="editor">
        <div class="title">
          <el-input placeholder="主题"
          v-model="form.title"></el-input>
        </div>
        <mavon-editor v-model="form.content"></mavon-editor>
        <div class="footer">
          <el-button type="primary" icon="el-icon-position" size="small"
          @click="onSubmit">提交</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
// import Editor from '../Editor.vue';

export default {
  name: 'NewDiscussion',
  components: {
    // Editor,
  },
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.$route.query.qid);
      this.axios.post(`/api/v1/questions/${this.$route.query.qid}/discussions`,
        this.form)
        .then((res) => {
          console.log(res);
        });
    },
  },
};
</script>

<style scoped>
.comment {
  margin-bottom: 15px;
}

.comment-header {
  height: 30px;
  margin-bottom: 10px;
}

.comment-user {
  line-height: 30px;
  font-size: 15px;
}

.editor {
  margin-top: 20px;
}
.title {
  margin-bottom: 10px;
}

.footer {
  display: flex;
  justify-content: flex-end;
}

</style>
