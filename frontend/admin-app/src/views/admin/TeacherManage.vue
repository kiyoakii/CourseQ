<template>
  <div class="teacher-manage">
    <div class="teacher-manage-header">
      <h2>教师名单</h2>
    </div>
    <div class="teacher-manage-content">
      <div id="flex-bar">
        <div class="flex-item">
          <admin-member-list-search id="stu-search" identity="teacher"></admin-member-list-search>
        </div>
        <div class="flex-item">
          <el-button type="primary" @click="onSubmit">注册新教师</el-button>
        </div>
      </div>
      <admin-member-list id="stu-list" :memberData="memberData"></admin-member-list>
    </div>
  </div>
</template>

<script>
import AdminMemberListSearch from '@/components/AdminMemberListSearch.vue';
import AdminMemberList from '@/components/AdminMemberList.vue';

export default {
  name: 'StudentManage',
  components: {
    AdminMemberListSearch,
    AdminMemberList,
  },
  data() {
    return {
      memberData: [],
    };
  },
  mounted() {
    this.axios.get('/v1/admin/admin/teacher-list')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.memberData = res.data.teachers;
      });
  },
  methods: {
    onSubmit() {
      console.log('submit!');
    },
  },
};
</script>

<style scoped>
.teacher-manage {
  flex: 1;
  padding: 30px;
}
.teacher-manage-header {
  padding: 0 100px;
}
.teacher-manage-content {
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
