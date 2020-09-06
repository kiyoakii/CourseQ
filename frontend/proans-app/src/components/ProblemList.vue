<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in problems" :key="index " class="infinite-list-item"
        @click="getProblem(problem.id)" >
        <el-card class="box-card card-h" shadow="hover"
        :class="selectedProblem === problem.id ? 'is-always-shadow active': ''">
          <div class="text item">
            <h2>{{ problem.title }}</h2>
            <render :markdown="problem.content" :transfer="true"></render>
          </div>
        </el-card>
      </li>
      <!-- <li v-if="problems.length === 0">
        <el-card class="box-card center card-h" shadow="hover">
          <span> 暂时没有问题噢 </span>
        </el-card>
      </li> -->
      <li @click="handleAdd" v-if="$route.params.tid !== '0'">
        <el-card class="box-card center" shadow="hover" style="font-size: 24px; color: #409EFF;"
          :class="selectedProblem === -2 ? 'is-always-shadow active': ''">
          <i class="el-icon-circle-plus-outline"></i>
        </el-card>
      </li>
    </ul>
  </div>
</template>

<script>
import Render from '@/components/Render.vue';

export default {
  name: 'ProblemList',
  components: {
    Render,
  },
  props: {
    problems: Array,
    searchInfo: String,
  },
  data() {
    return {
      count: 0,
      selectedProblem: -1,
      curTag: '',
      curInfo: '',
    };
  },
  computed: {
    qid() {
      console.log(this.$route.params.qid);
      return this.$route.params.qid;
    },
  },
  watch: {
    qid() {
      if (this.qid !== undefined) {
        this.selectedProblem = Number(this.qid);
      }
    },
    problems() {
      if (this.$route.params.tid === 'all'
      && this.$route.params.qid === undefined) {
        this.curTag = 'all';
      }
      if (this.$route.params.qid === undefined
      && (this.$route.params.tid !== this.curTag
        || this.searchInfo !== this.curInfo)
      && this.problems.length !== 0) {
        this.curInfo = this.searchInfo;
        this.curTag = this.$route.params.tid;
        this.$router.push({
          name: 'ProblemView',
          params: {
            cid: this.$route.params.cid,
            tid: this.$route.params.tid,
            qid: this.problems[0].id,
          },
        }).catch(() => {});
        this.$store.commit({
          type: 'setQid',
          id: Number(this.problems[0].id),
        });
      } else if (this.$route.params.tid === '0' || this.$route.name === 'IntroView') {
        this.selectedProblem = -1;
      }
    },
  },
  methods: {
    load() {
      this.count += 2;
    },
    getProblem(proid) {
      this.selectedProblem = proid;
      const problem = this.$store.getters.problem(proid);
      this.$router.push({
        name: 'ProblemView',
        params: {
          cid: this.$route.params.cid,
          tid: this.$route.params.tid || problem.tags[0].id,
          qid: proid,
        },
      }).catch(() => {});
    },
    handleAdd() {
      this.selectedProblem = -2;
      this.$router.push({
        name: 'AddProblemView',
        params: {
          cid: this.$route.params.cid,
          tid: this.$route.params.tid || -1,
          edit: false,
          problem: {
            title: '',
            tags: [this.$store.getters.tag(this.$route.params.tid) || { id: -1, name: '默认' }],
            content: '',
          },
        },
      }).catch(() => {});
    },
  },
};
</script>

<style scoped>
.box-card {
  margin-bottom: 15px;
  cursor: pointer;
}
.box-card:hover {
  background-color: #ecf5ff;
}
.active {
  /* background-color: #ecf5ff; */
  background: #ecf5ff;
  border-color: #b3d8ff;
}
.text {
  font-size: 12px;
}
/* .card-h {
  height: 120px;
} */
.link {
  text-decoration: none;
  color: #303133;
  display: block;
}
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}
.add-img {
  width: 40px;
}
</style>
