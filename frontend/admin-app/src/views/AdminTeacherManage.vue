<template>
  <div>
    <h2>教师名单</h2>
    <div id="flex-bar">
      <div class="flex-item">
        <admin-member-list-search id="stu-search" identity="teacher"></admin-member-list-search>
      </div>
      <div class="flex-item">
        <el-button type="primary" @click="onSubmit">注册新教师</el-button>
      </div>
    </div>
    <admin-member-list id="stu-list"></admin-member-list>
  </div>
</template>

<script>
import AdminMemberListSearch from '@/components/AdminMemberListSearch.vue';
import AdminMemberList from '@/components/AdminMemberList.vue';

export default {
  name: 'AdminStudentManage',
  components: {
    AdminMemberListSearch,
    AdminMemberList,
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
#stu-search {
  margin: 10px 0;
}
</style>
