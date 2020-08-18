<template>
  <el-card>
    <div class="comment-header">
        <div class="comment-title" v-show="!editEditorShow">{{ com.title }}</div>
        <div class="buttons" v-show="!editEditorShow">
          <el-button type="primary" size="small"
          @click="beforeEdit" icon="el-icon-edit" plain>编辑</el-button>
          <el-button type="primary" icon="el-icon-chat-dot-round" size="small"
            @click="beforeReply" plain>回复</el-button>
          <el-button type="danger" size="small"
              @click="handleDelete" icon="el-icon-delete" plain>删除</el-button>
        </div>
    </div>
    <div class="comment-body" v-show="!editEditorShow">
      <render :markdown="com.content"></render>
    </div>
    <div class="editor" v-show="editEditorShow">
      <el-input v-model="form.title"
        placeholder="标题"></el-input>
      <mavon-editor v-model="form.content"></mavon-editor>
      <div class="buttons">
        <el-button type="primary" icon="el-icon-close" size="small"
          @click="editEditorShow = false" plain></el-button>
        <el-button type="primary" icon="el-icon-position" size="small"
          @click="handleEdit" plain></el-button>
      </div>
    </div>
    <div class="editor" v-show="replyEditorShow">
      <mavon-editor v-model="form.content"></mavon-editor>
      <div class="buttons">
        <el-button type="primary" icon="el-icon-close" size="small"
          @click="replyEditorShow = false" plain></el-button>
        <el-button type="primary" icon="el-icon-position" size="small"
          @click="handleReply" plain></el-button>
      </div>
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
import Render from '@/components/Render.vue';
import CardReply from '@/components/Discussion/CardReply.vue';

export default {
  name: 'CardComment',
  components: {
    CardReply,
    Render,
  },
  props: {
    com: Object,
  },
  data() {
    return {
      replyEditorShow: false,
      editEditorShow: false,
      isShow: '',
      replyList: [
        {
          title: '1',
          content: 'askdjfhas',
          author_gid: '1',
          reply_id: '0',
        },
      ],
      form: {
        title: '',
        content: '',
      },
    };
  },
  methods: {
    beforeEdit() {
      this.form.title = this.com.title;
      this.form.content = this.com.content;
      this.editEditorShow = true;
    },
    handleEdit() {
      this.axios.put(`/api/v1/discussions/${this.com.id}`, this.form)
        .then((res) => {
          console.log(res);
          this.editEditorShow = false;
          this.com.title = this.form.title;
          this.com.content = this.form.content;
        });
    },
    beforeReply() {
      this.form.title = '';
      this.form.content = '';
      this.replyEditorShow = true;
    },
    handleReply() {
      console.log(this.form);
      this.axios.post(`/api/v1/discussions/${this.com.id}/answer`, { content: this.form.content })
        .then((res) => {
          console.log(res);
          this.replyEditorShow = false;
          this.updateData();
        });
    },
    handleDelete() {
      this.axios.delete(`/api/v1/discussions/${this.com.id}`)
        .then((res) => {
          console.log(res);
          this.$emit('deleteDiscussion', this.com.id);
        });
    },
    updateData() {
      this.axios.get(`/api/v1/discussions/${this.com.id}/answer`)
        .then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
            return;
          }
          this.replyList = res.data;
          console.log(this.replyList);
        });
    },
  },
  computed: {
    userAndTime() {
      return `${this.username}@${this.time}：`;
    },
  },
  mounted() {
    this.updateData();
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
  display: flex;
  justify-content: space-between;
  align-items: center;
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

.el-button {
  margin-left: 5px;
}
</style>
