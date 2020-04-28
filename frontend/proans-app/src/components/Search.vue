<template>
  <div>
    <el-input placeholder="请输入内容" v-model="searchText" class="input-with-select"
    @keyup.enter.native="search">
    <el-select v-model="select" slot="prepend" placeholder="类别">
      <el-option label="全部作业" value="0"></el-option>
      <el-option label="作业一" value="1"></el-option>
      <el-option label="作业二" value="2"></el-option>
      <el-option label="作业三" value="3"></el-option>
    </el-select>
    <!-- <el-button slot="append" icon="el-icon-search"></el-button> -->
  </el-input>
  </div>
</template>

<script>
export default {
  name: 'Search',
  data() {
    return {
      select: '',
      searchText: '',
    };
  },
  methods: {
    search() {
      console.log(this.select, this.searchText);
      // do some async functions here
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
