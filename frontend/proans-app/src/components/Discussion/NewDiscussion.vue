<template>
  <div>
    <el-card class="comment">
      <div class="comment-header">
        <el-row type="flex" justify="space-between">
          <div class="comment-user">新的讨论</div>
          <el-button type="primary" icon="el-icon-position" size="small"></el-button>
        </el-row>
      </div>
      <div class="comment-body">
        <editor></editor>
      </div>
    </el-card>
  </div>
</template>

<script>
import Editor from '../Editor.vue';

export default {
  name: 'NewDiscussion',
  components: {
    Editor,
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
