<template>
  <div>
    <el-input prefix-icon="el-icon-search"
    placeholder="请输入搜索内容" v-model="searchText"
    class="input-with-select"
    @input="search">
    <!-- <el-button slot="append" icon="el-icon-search"></el-button> -->
  </el-input>
  </div>
</template>

<script>
export default {
  name: 'Search',
  model: {
    prop: 'searchInfo',
    event: 'search',
  },
  data() {
    return {
      searchText: '',
      tid: '',
    };
  },
  watch: {
    $route() {
      this.tid = this.$route.params.tid;
    },
    tid() {
      this.searchText = '';
      this.$emit('search', this.searchText);
    },
  },
  methods: {
    search() {
      this.$emit('search', this.searchText);
    },
  },
};
</script>

<style scoped>
.el-select {
  width: 100px;
  font-size: 12px;
}
.el-select-dropdown__item {
  font-size: 12px;
}
</style>
