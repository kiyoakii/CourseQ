<template>
  <div class="student-manage">
    <div class="student-manage-header">
      <h2>学生名单</h2>
    </div>
    <div class="student-manage-content">
      <div id="flex-bar">
        <div class="flex-item">
          <admin-member-list-search id="stu-search" identity="student"></admin-member-list-search>
        </div>
        <div class="flex-item">
          <el-button type="primary" @click="onSubmit">注册新学生</el-button>
        </div>
      </div>
      <admin-member-list id="stu-list"></admin-member-list>
    </div>
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
.student-manage {
  flex: 1;
  padding: 30px;
}
.student-manage-header {
  padding: 0 100px;
}
.student-manage-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  padding: 10px 200px;
}
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
