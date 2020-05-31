<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in problems" :key="index " class="infinite-list-item">
        <el-card class="box-card" shadow="hover">
          <div slot="header" class="clearfix">
            <router-link :to="'/proans/1/problem/' + problem.id" class="link">
              <span>{{ problem.title }}</span>
            </router-link>
          </div>
          <div class="text item">
            {{ problem.content | formatDesc }}
          </div>
        </el-card>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ProblemList',
  props: {
    problems: [],
  },
  data() {
    return {
      count: 0,
    };
  },
  methods: {
    load() {
      this.count += 2;
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
</style>
