<template>
  <div>
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{ problem.title }}</span>
        <span class="tags" v-for="tag in problem.tags" :key="tag.id">
          <el-tag class="success" size="mini">{{ tag.name }}</el-tag>
        </span>
        <div class="stars">
          <img src="../assets/star-off.png" class="star-off"
          @click="handleStar" v-show="!starOn">
          <img src="../assets/star-on.png" class="star-on"
          @click="handleStar" v-show="starOn">
          <span >{{ stars }}</span>
        </div>
      </div>
      <div class="text item">
        <render :markdown="problem.content"></render>
      </div>
      <div class="footer">
        <div class="edit-info">
          <span>{{ problem.author.nickname }} 于
            {{ (new Date(problem.update_datetime))
            .toLocaleString('zh-CN', { hour12: false }) }} 修改</span>
        </div>
        <div class="buttons">
          <el-button size="small" type="primary"
          @click="handleEdit" icon="el-icon-edit"
          plain
          :disabled="disableInteract"
          >编辑</el-button>
          <el-button slot="reference" size="small" type="danger"
            icon="el-icon-delete" plain
            :disabled="disableInteract || !isAuthorOrTeacher"
            @click="handleDelete"
            >删除</el-button>
        </div>
      </div>
    </el-card>
  </div>
</template>

<script>
import Render from '@/components/Render.vue';
import { instance } from '../helpers/instances';
// import { debounce } from '../helpers/utils';

function syncProblem(self) {
  let timer = null;
  return () => {
    clearTimeout(timer);
    if (self.starOn === self.problem.liked) {
      return;
    }
    timer = setTimeout(() => {
      instance.post(`/api/v1/questions/${self.problem.id}/like`, {
        liked: self.starOn,
      }).then(() => {
        self.$emit('updateProblem');
      }).catch(() => {
        // self.starOn = self.problem.liked;
      });
    }, 500);
  };
}

export default {
  name: 'ProblemCard',
  components: {
    Render,
  },
  props: {
    problem: {
      type: Object,
      default() {
        return {
          title: '',
          tags: [],
          content: '',
          author: {
            nickname: '',
          },
        };
      },
    },
  },
  data() {
    return {
      popoverVisible: false,
      starOn: false,
      stars: 0,
      syncProblem: syncProblem(this),
    };
  },
  computed: {
    disableInteract() {
      return !this.problem.history;
    },
    isAuthorOrTeacher() {
      return this.problem.author.gid === this.$store.state.gid
        || this.$store.state.auth !== '学生';
    },
  },
  watch: {
    problem() {
      this.stars = this.problem.stars;
      this.starOn = this.problem.liked;
    },
  },
  methods: {
    handleDelete() {
      this.$confirm('确认删除？')
        .then((_) => {
          console.log(_);
          instance.delete(`/api/v1/questions/${this.problem.id}`)
            .then((res) => {
              console.log(res);
              this.popoverVisible = false;
              if (res.status !== 200) {
                console.log(JSON.stringify(res.data));
              }
              this.$store.commit('deleteProblem', this.problem);
              this.$router.push({
                name: 'CategoryView',
                params: {
                  cid: this.$route.params.cid,
                  tid: this.$route.params.tid,
                  problem: this.problem,
                  edit: true,
                },
              });
            });
        })
        .catch((_) => { console.log(_); });
    },
    handleEdit() {
      this.axios({
        method: 'POST',
        url: `/api/v1/questions/${this.$route.params.qid}/lock`,
      }).then((res) => {
        if (res.status === 403) {
          this.$message.info('对不起，该问题已被其他用户编辑，请等待.');
          return;
        }
        this.$router.push({
          name: 'EditProblemView',
          params: {
            cid: this.$route.params.cid,
            tid: this.$route.params.tid,
            qid: this.$route.params.qid,
            problem: this.problem,
            edit: true,
          },
        });
      });
    },
    handleStar() {
      if (this.disableInteract) {
        this.$message.error('对不起，历史版本不能点赞！');
        return;
      }
      if (this.starOn) {
        // this.problem.liked = false;
        this.starOn = false;
        if (this.stars > 1) {
          this.stars -= 1;
        } else {
          this.stars = 0;
        }
      } else {
        // this.problem.liked = true;
        this.starOn = true;
        this.stars += 1;
      }
      this.syncProblem();
    },
  },
  beforeMount() {
    this.axios.defaults.headers.common.Authorization = `Bearer ${this.$store.state.proansToken}`;
  },
};
</script>

<style scoped>
.tags {
  margin-left: 0px;
  margin-right: 10px;
  border: 3px;
}
.el-tag {
  font-size: 10px;
}
.title {
  font-size: 18px;
  margin-left: 0px;
  margin-right: 10px;
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
.star-off {
  width: 20px;
  margin-right: 5px;
  margin-left: 20px;
}
.star-on {
  width: 20px;
  margin-right: 7px;
}
.el-button {
  margin-left: 5px;
}
</style>
