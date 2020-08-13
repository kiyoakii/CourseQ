<template>
  <el-card>
    <div class="comment-header">
      <el-row type="flex" justify="space-between">
        <div class="comment-title">{{ com.title }}</div>
        <div>
          <div v-show="!editorShow">
            <el-button type="primary" icon="el-icon-edit" size="small"
              @click="editorShow = true">回复</el-button>
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
      {{ com.content }}
    </div>
    <div class="comment-editor" v-show="editorShow">
      <editor></editor>
    </div>
    <el-collapse accordion v-model="isShow">
      <el-collapse-item>
        <template slot="title">
          <i class="header-icon el-icon-chat-dot-round"></i>
          <span class="reply-header">查看回复</span>
        </template>
        <div v-for="(rep, index) in replyList" :key="index">
          <card-reply class="reply"
            :content="rep.content">
          </card-reply>
        </div>
        <div v-if="replyList.length == 0">暂时没有回复噢</div>
      </el-collapse-item>
    </el-collapse>
  </el-card>
</template>

<script>
import Editor from '@/components/Editor.vue';
import CardReply from '@/components/Discussion/CardReply.vue';

export default {
  name: 'CardComment',
  components: {
    Editor,
    CardReply,
  },
  props: {
    com: Object,
  },
  data() {
    return {
      editorShow: false,
      isShow: '',
      replyList: [
        {
          title: '1',
          content: 'askdjfhas',
          author_gid: '1',
          reply_id: '0',
        },
      ],
    };
  },
  computed: {
    userAndTime() {
      return `${this.username}@${this.time}：`;
    },
  },
  mounted() {
    this.axios.get(`/api/v1/discussions/${this.com.id}/answer`)
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.replyList = res.data;
      });
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

.comment-title {
  line-height: 30px;
  font-size: 18px;
}

.reply {
  margin-bottom: 10px;
}

.reply-header {
  font-size: 14px;
}
</style>
