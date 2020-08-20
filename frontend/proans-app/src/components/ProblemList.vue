<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in problems" :key="index " class="infinite-list-item"
        @click="getProblem(problem.id)" >
        <el-card class="box-card" shadow="hover"
        :class="selectedProblem === problem.id ? 'is-always-shadow active': ''">
          <div slot="header" class="clearfix">
            <span>{{ problem.title }}</span>
          </div>
          <div class="text item">
            <render :markdown="problem.content | formatDesc"></render>
          </div>
        </el-card>
      </li>
      <li @click="handleAdd">
        <el-card class="box-card center" shadow="hover" style="font-size: 30px; color: #409EFF;">
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
  },
  data() {
    return {
      count: 0,
      selectedProblem: -1,
    };
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
  filters: {
    formatDesc(value) {
      const reg = new RegExp('.*!\\[.*]\\(.*\\)');
      value = value.replace(reg, '「图片」');
      return value.length <= 50 ? value : `${value.slice(0, 50)}...`;
    },
  },
};
</script>

<style scoped>
.box-card {
  font-weight: 600;
  margin-bottom: 15px;
  cursor: pointer;
}

.box-card:hover {
  background: rgba(250, 250, 250, .8);
}
.active {
  background: rgba(250, 250, 250, .8);
}
.text {
  font-size: 12px;
}

.link {
  text-decoration: none;
  color: #303133;
  display: block;
}
.center {
  display: flex;
  justify-content: center;
}
.add-img {
  width: 40px;
}
</style>
