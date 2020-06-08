<template>
  <div>
    <el-card>
      <el-collapse accordion v-model="isShow">
        <el-collapse-item title="讨论区" name="1">
          <div v-for="(com, index) in commentList" :key="index">
            <card-comment class="comment"
              :username="com.username"
              :time="com.date"
              :comment="com.content">
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
      commentList: [],
    };
  },
  mounted() {
    this.axios.get('/v1/proans/discussions?id=1&problem=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.commentList = res.data.data.discussions;
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
