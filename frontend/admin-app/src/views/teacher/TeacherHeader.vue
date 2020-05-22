<template>
  <el-row class="header" type="flex" justify="space-between">
    <el-col :span="2">
      <div class="center">
        <!-- In Vue tmplate, import an image is tricky， we use webpack require syntax here -->
        <div class="logo-img"
        :style="{ backgroundImage: 'url(' + require('@/assets/logo.png') + ')' }">
        </div>
      </div>
    </el-col>
    <el-col>
      <teacher-nav-bar></teacher-nav-bar>
    </el-col>
    <el-col :span="2">
      <div class="center">
        <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
      </div>
    </el-col>
  </el-row>
</template>

<script>
import TeacherNavBar from '@/components/TeacherNavBar.vue';

export default {
  name: 'TeacherHeader',
  components: {
    TeacherNavBar,
  },
};
</script>

<style scoped>
.header {
  height: 100%;
}

.center {
  height: 100%;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}

.logo-img {
  height: 40px;
  width: 40px;
  background-size: contain;
  background-repeat: no-repeat;
}
</style>
