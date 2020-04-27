<template>
  <el-card>
    <div class="comment-header">
      <el-row type="flex" justify="space-between">
        <div class="comment-user">{{ username }}@{{ time }}：</div>
        <div>
          <div v-show="!editorShow">
            <el-button type="primary" icon="el-icon-edit" size="small"
              @click="editorShow = true"></el-button>
          </div>
          <div v-show="editorShow">
            <el-button type="primary" icon="el-icon-close" size="small"
              @click="editorShow = false"></el-button>
            <el-button type="primary" icon="el-icon-position" size="small"
              ></el-button>
          </div>
        </div>
      </el-row>
    </div>
    <div class="comment-body">
      {{ comment }}
    </div>
    <div class="comment-editor" v-show="editorShow">
      <editor></editor>
    </div>
  </el-card>
</template>

<script>
import Editor from '@/components/Editor.vue';

export default {
  name: 'CardComment',
  components: {
    Editor,
  },
  props: {
    username: {
      type: String,
    },
    time: {
      type: String,
    },
    comment: {
      type: String,
    },
  },
  data() {
    return {
      editorShow: false,
    };
  },
  computed: {
    userAndTime() {
      return `${this.username}@${this.time}：`;
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
</style>
