<template>
  <div>
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{ problem.title }}</span>
        <span class="tags" v-for="tag in problem.tags" :key="tag.id">
          <el-tag class="success" size="mini">{{ tag.name }}</el-tag>
        </span>
        <div class="stars">
          <img src="../assets/star-off.png" class="star"
          @click="handleStar" v-show="!starOn">
          <img src="../assets/star-on.png" class="star"
          @click="handleStar" v-show="starOn">
          <span >{{ problem.stars }}</span>
          <i class="el-icon-star-off star"></i>
        </div>
      </div>
      <div class="text item">
        {{ problem.content }}
      </div>
      <div class="footer">
        <div class="edit-info">
          <span>{{ problem.author.nickname }} 于
            {{ (new Date(problem.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC'}) }} 修改</span>
        </div>
        <div class="buttons">
          <el-button size="medium"
          @click="handleEdit">编辑</el-button>
          <el-popover
          placement="top"
          width="160"
          v-model="popoverVisible">
          <p>确定删除吗？</p>
          <div style="text-align: right; margin: 0">
            <el-button size="mini" type="text" @click="popoverVisible = false">取消</el-button>
            <el-button type="primary" size="mini" @click="handleDelete">确定</el-button>
          </div>
          <el-button slot="reference">删除</el-button>
        </el-popover>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>

export default {
  name: 'ProblemCard',
  props: {
    problem: {
      type: Object,
      default() {
        return {
          title: '',
          tags: [],
          content: '',
        };
      },
    },
  },
  data() {
    return {
      popoverVisible: false,
      starOn: false,
    };
  },
  methods: {
    handleDelete() {
      this.axios.delete(`/api/v1/questions/${this.problem.id}`)
        .then((res) => {
          console.log(res);
          this.popoverVisible = false;
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
          }
        });
    },
    handleEdit() {
      this.$router.push({
        path: '/proans/',
        name: 'EditView',
        params: {
          problem: this.problem,
          edit: true,
        },
        query: {
          tid: this.$route.query.tid,
        },
      });
    },
    handleStar() {
      if (this.starOn) {
        this.starOn = false;
        this.axios.post(`/api/v1/questions/${this.problem.id}/like`)
          .then((res) => {
            console.log(res);
            this.popoverVisible = false;
            if (res.status !== 200) {
              console.log(JSON.stringify(res.data));
            }
          });
      } else {
        this.starOn = true;
        this.axios.post(`/api/v1/questions/${this.problem.id}/like`)
          .then((res) => {
            console.log(res);
            this.popoverVisible = false;
            if (res.status !== 200) {
              console.log(JSON.stringify(res.data));
            }
          });
      }
    },
  },
};
</script>

<style scoped>
.tags {
  margin-left: 10px;
}
.el-tag {
  font-size: 10px;
}
.title {
  font-size: 18px;
}
.footer {
  padding-top: 20px;
  display: flex;
  justify-content:space-between;
  align-items: flex-end;
}
.stars {
  float: right;
  font-size: 16px;
  display: flex;
  align-items: center;
}
.edit-info {
  font-size: 12px;
  color: #606266;
}
.star {
  width: 20px;
  margin-right: 5px;
  margin-left: 20px;
}
</style>
