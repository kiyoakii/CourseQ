<template>
  <div>
    <el-card>
      <div slot="header" class="clearfix">
        <span class="title">讨论区</span>
      </div>
      <div v-for="(com, index) in commentList" :key="index">
        <card-comment class="comment"
          :com="com"
          @deleteDiscussion="handleDelete">
        </card-comment>
      </div>
      <div v-if="commentList.length == 0" class="comment">
        暂时没有讨论哦，快来发起第一个讨论吧
      </div>
      <div class="new-discussion">
        <new-discussion @createDiscussion="handleCreate"></new-discussion>
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
    commentList: Array,
  },
  data() {
    return {
      isShow: '',
      editorShow: false,
    };
  },
  methods: {
    handleDelete(did) {
      this.commentList.splice(this.commentList.findIndex((c) => c.id === did), 1);
    },
    handleCreate(d) {
      this.commentList.push(d);
    },
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
