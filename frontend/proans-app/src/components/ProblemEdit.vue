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
        <editor class="mavon-editor" v-model="form.content"></editor>
      </div>
      <div style="display: flex; justify-content: flex-end;">
        <el-button type="primary" icon="el-icon-close" size="small"
          @click="closeEditor" plain>取消</el-button>
        <el-button type="primary" icon="el-icon-position" size="small"
          @click="onSubmit" plain>确定</el-button>
      </div>
    </el-card>
  </div>
</template>

<script>
import Editor from '@/components/Editor.vue';
import { instance } from '../helpers/instances';

export default {
  name: 'ProblemEdit',
  components: {
    Editor,
  },
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
      lockTimer: 0,
      lockTimes: 0,
    };
  },
  methods: {
    handleClose(tag) {
      if (tag === '默认' && this.form.tags.length === 1) {
        this.$message.error('问题至少有一个 tag!');
        return;
      }
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
    closeEditor() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/unlock`,
      }).then(() => {
        clearInterval(this.lockTimer);
        this.$router.push({
          name: 'ProblemView',
          params: {
            cid: this.$route.params.cid,
            tid: this.$route.params.tid,
            qid: this.$route.params.qid,
          },
        });
      });
    },
    onSubmit() {
      if (this.edit) {
        instance.put(`/api/v1/questions/${this.$route.params.qid}`,
          {
            title: this.form.title,
            content: this.form.content,
            new_tags: this.form.tags,
            old_tags: this.oldTags,
          })
          .then((res) => {
            if (res.status !== 200) {
              console.log(JSON.stringify(res.data));
            }
            this.$store.commit('updateProblem', this.$route.params.problem);
            this.closeEditor();
          });
      } else {
        console.log(this.form);
        instance.post(`/api/v1/courses/${this.$route.params.cid}/questions`, {
          title: this.form.title,
          content: this.form.content,
          tags: this.form.tags.length === 0 ? ['默认'] : this.form.tags,
        }).then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
          }
          this.$store.dispatch('initProblems');
          this.$router.push({
            name: 'CategoryView',
            params: {
              cid: this.$route.params.cid,
              tid: this.$route.params.tid,
            },
          });
        });
      }
    },
  },
  beforeDestory() {
    clearInterval(this.lockTimer);
  },
  mounted() {
    this.axios.defaults.headers.common.Authorization = `Bearer ${this.$store.state.proansToken}`;
    console.log(this.$route);
    this.form.title = this.$route.params.problem.title;
    this.form.content = this.$route.params.problem.content;
    this.$route.params.problem.tags.forEach((t) => this.form.tags.push(t.name));
    this.$route.params.problem.tags.forEach((t) => this.oldTags.push(t.name));
    this.edit = this.$route.params.edit;
    if (this.edit) {
      this.lockTimer = setInterval(() => {
        this.axios({
          method: 'POST',
          url: `/api/v1/questions/${this.$route.params.qid}/lock`,
        }).then((res) => {
          this.lockTimes += 1;
          if (this.lockTimes > 40) {
            this.$message.info('由于长时间未改动，你即将退出编辑界面.');
            clearInterval(this.lockTimer);
            this.axios.post(`/v1/questions/${this.$route.params.qid}/unlock`)
              .then(() => {
                this.$router.push({
                  name: 'ProblemView',
                  params: {
                    cid: this.$route.params.cid,
                    tid: this.$route.params.tid,
                    qid: this.$route.params.qid,
                  },
                });
              });
            return;
          }
          if (res.status === 403) {
            this.$message.info('对不起，该问题已被其他用户编辑，请等待.');
            clearInterval(this.lockTimer);
            this.$nextTick(() => {
              this.$router.push({
                name: 'ProblemView',
                params: {
                  cid: this.$route.params.cid,
                  tid: this.$route.params.tid,
                  qid: this.$route.params.qid,
                },
              });
            });
          }
        });
      }, 1000 * 15);
    }
  },
};
</script>

<style scoped>
.el-tag {
  margin-right: 10px;
  margin-bottom: 10px;
}
.button-new-tag {
  margin-right: 10px;
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
