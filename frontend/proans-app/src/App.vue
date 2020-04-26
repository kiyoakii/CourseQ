<template>
  <div id="app">
    <el-container>
      <el-header>
        <vue-header></vue-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-col :xs="24" :sm="24" :md="22" :lg="18" :xl="18" >
            <vue-content></vue-content>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import VueHeader from './views/VueHeader.vue';
import VueContent from './views/VueContent.vue';

export default {
  name: 'app',
  components: {
    VueHeader,
    VueContent,
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
