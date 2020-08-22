<template>
  <div id="app">
    <el-container>
      <el-header>
        <vue-header></vue-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-col :xs="24" :sm="24" :md="22" :lg="22" :xl="22" >
            <vue-content></vue-content>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import VueHeader from '@/views/VueHeader.vue';
import VueContent from '@/views/VueContent.vue';

export default {
  name: 'app',
  components: {
    VueHeader,
    VueContent,
  },
  beforeCreate() {
    const currentUrl = window.location.href;
    const serviceUrl = 'http://home.ustc.edu.cn/~jarvis/cas/index.html';
    console.log(currentUrl);
    this.$store.state.token = '';
    if (currentUrl.includes('ticket')) {
      console.log(222);
      const ticket = currentUrl.match(/ticket=([\s\S]+?)/)[1];
      const service = currentUrl.match(/service=([\s\S]+?)/)[1];
      this.axios.get(`/api/v1/token?id=null&ticket=${ticket}&service=${service}`)
        .then((res) => {
          if (res.status === 200) {
            this.$store.commit('setToken', res.data.access_token);
            window.location.href = currentUrl.slice(0, currentUrl.indexOf('?'));
          }
        });
    } else if (!this.$store.state.token) {
      const redirectUrl = window.location.href;
      const casUrl = `http://passport.ustc.edu.cn/login?service=${serviceUrl}?redirect=${redirectUrl}`;
      window.location.href = casUrl;
    }
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}

#app {
  font-family: BlinkMacSystemFont, Helvetica Neue, PingFang SC, Microsoft YaHei, Source Han Sans SC,
               Noto Sans CJK SC, WenQuanYi Micro Hei, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-size: 16px;
}

.el-header {
  padding: 0 !important;
  border-bottom: 1px solid #eeeeee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
</style>
