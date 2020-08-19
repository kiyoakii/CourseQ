<template>
  <div>
    <div class="title">
      <el-input placeholder="请输入讨论主题"
      v-model="form.title"></el-input>
    </div>
    <editor v-model="form.content" :autofocus="false"></editor>
    <div class="footer">
      <div class="buttons">
        <el-button type="primary" icon="el-icon-close" size="small"
          @click="$emit('update:show', false);" plain>取消</el-button>
        <el-button type="primary" icon="el-icon-position" size="small"
          @click="submitForm" plain>确定</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import Editor from '../Editor.vue';
import { instance } from '../../helpers/instances';

export default {
  name: 'NewDiscussion',
  components: {
    Editor,
  },
  data() {
    return {
      form: {
        title: '',
        content: '',
      },
    };
  },
  props: {
    show: {
      type: Boolean,
    },
  },
  methods: {
    submitForm() {
      const self = this;
      instance.post(`/api/v1/questions/${this.$route.params.qid}/discussions`,
        this.form)
        .then(() => {
          self.$store.dispatch('setCommentList');
        });
      this.form = {
        title: '',
        content: '',
      };
      this.$emit('update:show', false);
    },
  },
};
</script>

<style scoped>

.title {
  margin-bottom: 20px;
}

.footer {
  display: flex;
  justify-content: flex-end;
}

</style>
