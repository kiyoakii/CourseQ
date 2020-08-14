<template>
  <div>
    <el-input
      placeholder="请输入想要搜索的信息"
      @input="(value) => $emit('input', value)"
      :value="value"
      prefix-icon="el-icon-search">
      </el-input>
  </div>
</template>

<script>
export default {
  name: 'DataTableSearchBar',
  props: {
    value: {
      type: String,
      default: '',
    },
  },
};
</script>

<style scoped>
.form-item {
  margin-bottom: 0;
}
</style>
