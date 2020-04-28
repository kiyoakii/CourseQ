<template>
  <div>
    <el-card>
      <el-collapse accordion v-model="isShow">
        <el-collapse-item title="讨论区" name="1">
          <div v-for="(com, index) in commentList" :key="index">
            <card-comment class="comment"
              :username="com.username"
              :time="com.time"
              :comment="com.comment">
            </card-comment>
          </div>
          <div class="new-discussion">
            <new-discussion></new-discussion>
          </div>
        </el-collapse-item>
      </el-collapse>
      <div class="last-comment" v-show="isShow == ''">
        我觉得应该这样。<br>
        不要你觉得，我要我觉得。
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
  data() {
    return {
      isShow: '',
      editorShow: false,
      commentList: [
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
        {
          username: '小王',
          time: '2019/12/12',
          comment: `
              动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。
              动态 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。
          `,
        },
      ],
    };
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
