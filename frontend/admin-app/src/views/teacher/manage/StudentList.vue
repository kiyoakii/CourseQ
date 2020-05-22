<template>
  <div>
    <h2>学生名单</h2>
    <div id="flex-bar">
      <div class="flex-item">
        <member-list-search id="ta-search"></member-list-search>
      </div>
      <div class="flex-item">
        <el-button type="primary" @click="onSubmit">添加学生</el-button>
      </div>
    </div>
    <member-list id="ta-list"></member-list>
  </div>
</template>

<script>
import MemberListSearch from '@/components/MemberListSearch.vue';
import MemberList from '@/components/MemberList.vue';

export default {
  name: 'StudentList',
  components: {
    MemberListSearch,
    MemberList,
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },
  },
};
</script>

<style scoped>
#flex-bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
#ta-search {
  margin: 10px 0;
}
</style>
