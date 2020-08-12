<template>
  <el-card>
    <div class="reply-header">
      <el-row type="flex" justify="space-between">
        <div class="reply-title">{{ title }}用户1234：</div>
      </el-row>
    </div>
    <div class="reply-body">
      {{ content }}
      这里是内容
    </div>
  </el-card>
</template>

<script>
export default {
  name: 'CardReply',
  components: {
  },
  props: {
    title: {
      type: String,
    },
    author_gid: {
      type: String,
    },
    stars: {
      type: Number,
    },
    content: {
      type: String,
    },
  },
  data() {
    return {
      isShow: false,
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
.reply {
  margin-bottom: 15px;
}

.reply-header {
  height: 30px;
  margin-bottom: 10px;
}

.reply-title {
  line-height: 30px;
  font-size: 14px;
}

.reply-body {
    font-size: 14px;
}

</style>
