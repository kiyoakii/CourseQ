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

<style>

</style>
