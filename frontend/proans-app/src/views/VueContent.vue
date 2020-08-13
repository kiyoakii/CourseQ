<template>
  <div>
    <el-container>
      <el-aside>
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
