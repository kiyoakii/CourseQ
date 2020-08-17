<template>
  <div>
    <el-container>
      <el-aside style="padding-top: 20px;">
        <router-view name="sidebar"></router-view>
      </el-aside>
      <el-main>
        <router-view ></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>

export default {
  name: 'VueContent',
  components: {
  },
};
</script>

<style>

</style>
