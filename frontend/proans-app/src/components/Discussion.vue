<template>
  <div>
    <el-card>
      <div slot="header" class="clearfix">
        <span class="title">讨论区</span>
      </div>
      <div v-for="(com, index) in commentList" :key="index">
        <card-comment class="comment"
          :title="com.title"
          :content="com.content">
        </card-comment>
      </div>
      <div class="new-discussion">
        <new-discussion></new-discussion>
      </div>
    </el-card>
  </div>
</template>

<script>
import CardComment from './Discussion/CardComment.vue';
import NewDiscussion from './Discussion/NewDiscussion.vue';

export default {
  name: 'Discussion',
  components: {
    CardComment,
    NewDiscussion,
  },
  props: {
    qid: {
      type: String,
      default() {
        return '2';
      },
    },
  },
  data() {
    return {
      isShow: '',
      editorShow: false,
      commentList: [],
    };
  },
  mounted() {
    this.axios.get(`/api/v1/questions/${this.qid}/discussions`)
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.commentList = res.data;
      });
  },
};
</script>

<style>
div.el-collapse, div.el-collapse-item {
  border: none;
}

div.el-collapse-item__header {
  font-size: 16px;
}

div.el-collapse-item__wrap {
  border: none;
}

.last-comment {
  margin-top: 5px;
  font-size: 13px;
  line-height: 24px;
}

.comment {
  margin-bottom: 20px;
}

</style>
