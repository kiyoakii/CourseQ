<template>
  <div>
    <el-card>
      <div class="editor">
        <div class="title">
          <el-input placeholder="主题"
          v-model="form.title"></el-input>
        </div>
        <el-tag
          :key="tag"
          v-for="tag in form.tags"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)">
          {{ tag }}
        </el-tag>
        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small"
        @click="showInput">+ New Tag</el-button>
        <mavon-editor class="mavon-editor" v-model="form.content"></mavon-editor>
      </div>
      <div class="footer">
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'ProblemEdit',
  data() {
    return {
      form: {
        title: '',
        content: '',
        tags: [],
      },
      oldTags: [],
      formLabelWidth: '120px',
      inputVisible: false,
      inputValue: '',
      edit: false,
    };
  },
  methods: {
    handleClose(tag) {
      this.form.tags.splice(this.form.tags.indexOf(tag), 1);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick((_) => {
        console.log(_);
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      if (this.inputValue) {
        this.form.tags.push(this.inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    onSubmit() {
      if (this.edit) {
        console.log('oldTags', this.oldTags, 'newTags', this.form.tags);
        this.axios.put(`/api/v1/questions/${this.$route.params.problem.id}`,
          {
            title: this.form.title,
            content: this.form.content,
            new_tags: this.form.tags,
            old_tags: this.oldTags,
          })
          .then((res) => {
            console.log(res);
            if (res.status !== 200) {
              console.log(JSON.stringify(res.data));
            }
            this.$store.commit('updateProblem', this.$route.params.problem);
            console.log('成功');
            this.$router.push({
              path: '/proans/',
              name: 'ProblemView',
              query: {
                tid: this.$route.query.tid,
                qid: this.$route.params.problem.id,
              },
            });
          });
      } else {
        console.log(this.form);
        this.axios.post('/api/v1/courses/6/questions', this.form)
          .then((res) => {
            console.log(res);
            if (res.status !== 200) {
              console.log(JSON.stringify(res.data));
            }
            this.$store.dispatch('initProblems');
            this.$router.push({
              path: '/proans',
              name: 'CategoryView',
              query: {
                tid: this.$route.query.tid,
              },
            });
          });
      }
    },
  },
  mounted() {
    this.form.title = this.$route.params.problem.title;
    this.form.content = this.$route.params.problem.content;
    this.$route.params.problem.tags.forEach((t) => this.form.tags.push(t.name));
    this.$route.params.problem.tags.forEach((t) => this.oldTags.push(t.name));
    this.edit = this.$route.params.edit;
  },
};
</script>

<style scoped>
.el-tag + .el-tag {
  margin-left: 10px;
}
.button-new-tag {
  margin-left: 10px;
  height: 32px;
  line-height: 30px;
  padding-top: 0;
  padding-bottom: 0;
}
.input-new-tag {
  width: 90px;
  margin-left: 10px;
  vertical-align: bottom;
}
.footer {
  display: flex;
  justify-content: flex-end;
}

.title {
  margin: 10px 0;
}
.mavon-editor {
  margin: 20px 0;
}
</style>
