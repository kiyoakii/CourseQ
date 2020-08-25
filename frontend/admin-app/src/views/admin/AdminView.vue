<template>
  <div>
    <el-container>
      <el-header>
        <admin-header></admin-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-col :md="24" :lg="23">
            <admin-content></admin-content>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import AdminHeader from '@/views/admin/AdminHeader.vue';
import AdminContent from '@/views/admin/AdminContent.vue';

export default {
  name: 'AdminView',
  components: {
    AdminHeader,
    AdminContent,
  },
};
</script>

<style scoped>

.el-header {
  padding: 0 !important;
  border-bottom: 1px solid #eeeeee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

</style>
