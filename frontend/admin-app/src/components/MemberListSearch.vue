<template>
  <div>
    <el-form :inline="true" :model="searchForm">
      <el-form-item class="form-item">
        <el-input v-model="searchForm.name" placeholder="姓名"></el-input>
      </el-form-item>
      <el-form-item class="form-item">
        <el-input v-model="searchForm.id" placeholder="学号"></el-input>
      </el-form-item>
      <el-form-item class="form-item">
        <el-button type="primary" @click="onSubmit">查询</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: 'MemberListSearch',
  data() {
    return {
      searchForm: {
        name: '',
        id: '',
      },
    };
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },
  },
};
</script>

<style scoped>
.form-item {
  margin-bottom: 0;
}
</style>
