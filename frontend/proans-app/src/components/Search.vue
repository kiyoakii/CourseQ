<template>
  <div>
    <el-input placeholder="请输入内容" v-model="searchText"
    class="input-with-select"
    @keyup.enter.native="search">
    <el-select v-model="select" slot="prepend" placeholder="类别">
      <el-option v-for="tag in tags" :key="tag.id"
      :label="tag.name" :value="tag.id"></el-option>
    </el-select>
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
  props: {
    tags: {
      type: Array,
      default() {
        return [];
      },
    },
  },
  data() {
    return {
      select: '',
      searchText: '',
    };
  },
  methods: {
    search() {
      console.log(this.select, this.searchText);
      this.$emit('search', { select: this.select, searchText: this.searchText });
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
