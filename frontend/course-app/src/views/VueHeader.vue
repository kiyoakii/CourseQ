<template>
  <el-row>
    <el-col :span="8">
      <div class="logo">
        <!-- In Vue tmplate, import a image is tricky， we use webpack require syntax here -->
        <div class="logo-img"
        :style="{ backgroundImage: 'url(' + require('@/assets/logo.png') + ')' }">
        </div>
        {{allinfo.name_zh}} - {{allinfo.semester}}
      </div>
    </el-col>
    <el-col :span="16">
      <nav-bar :allinfo="allinfo"></nav-bar>
    </el-col>
  </el-row>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'VueHeader',
  props: {
    allinfo: {},
  },
  components: {
    NavBar,
  },
};
</script>

<style scoped>
.logo {
  line-height: 60px;
  height: 60px;
  text-align: center;
  border-bottom: solid 1px #e6e6e6;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: 400;
  font-size: 14px;
  color: gray;
}
.logo-img {
  height: 40px;
  width: 80px;
  background-size: contain;
  background-repeat: no-repeat;
  /* transform: rotate(180deg); */
}
</style>
