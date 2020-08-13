<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in problems" :key="index " class="infinite-list-item"
        @click="getProblem(problem.id)" >
        <el-card class="box-card" shadow="hover"
        :class="{selected:selectedProblem === problem.id}">
          <div slot="header" class="clearfix">
            <span>{{ problem.title }}</span>
          </div>
          <div class="text item">
            {{ problem.content | formatDesc }}
          </div>
        </el-card>
      </li>
      <li @click="handleAdd">
        <el-card class="box-card center" shadow="hover">
          <img src="@/assets/add.png" class="add-img">
        </el-card>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ProblemList',
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
      this.$router.push({
        path: '/proans/',
        name: 'CategoryView',
        query: {
          tid: this.$route.query.tid,
          qid: proid,
        },
      });
    },
    handleAdd() {
      this.$router.push({
        path: '/proans/',
        name: 'AddProblemView',
        query: {
          tid: this.$route.query.tid,
        },
        params: {
          edit: false,
          problem: {
            title: '',
            tags: [this.$store.getters.tag(this.$route.query.tid)],
            content: '',
          },
        },
      });
    },
  },
  filters: {
    formatDesc(value) {
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

.text {
  font-size: 12px;
}

.link {
  text-decoration: none;
  color: #303133;
  display: block;
}
.selected {
  background-color: #ecf5ff;
}
.center {
  display: flex;
  justify-content: center;
}
.add-img {
  width: 40px;
}
</style>
