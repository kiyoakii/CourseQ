<template>
  <el-row class="header" type="flex" justify="space-between">
    <el-col :span="4">
      <div class="logo">
        <!-- In Vue tmplate, import a image is tricky， we use webpack require syntax here -->
        <div class="logo-img"
        :style="{ backgroundImage: 'url(' + require('@/assets/logo.png') + ')' }">
        </div>
      </div>
    </el-col>
    <el-col :span="2">
      <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
    </el-col>
  </el-row>
</template>

<script>

export default {
  name: 'VueHeader',
  components: {
  },
};
</script>

<style scoped>
.header {
  margin: 10px 0;
}

.logo {
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.logo-img {
  height: 40px;
  width: 80px;
  background-size: contain;
  background-repeat: no-repeat;
}
</style>
