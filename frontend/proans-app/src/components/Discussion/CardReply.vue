<template>
  <el-row class="card-reply">
    <render :markdown="reply.content" style="display: inline-box"/>
    <el-divider content-position="right">
      <span class="reply-title">{{ reply.author?
        (reply.author.nickname || reply.author.gid) : '' }} 回复</span>
    </el-divider>
  </el-row>
</template>

<script>
import Render from '../Render.vue';

export default {
  name: 'CardReply',
  components: {
    Render,
  },
  props: {
    reply: {
      type: Object,
      default() {
        return {
          author: {
            type: Object,
            default() {
              return {
                nickname: '',
                gid: '',
              };
            },
          },
        };
      },
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

.card-reply {
  padding-left: 2em;
}

</style>
