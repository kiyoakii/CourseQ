<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'app',
  beforeMount() {
    const currentUrl = window.location.href;
    if (currentUrl.includes('hashparam')) {
      window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}#${currentUrl.match(/hashparam=([\s\S]+)#\//)[1]}`;
    }
    const appPath = currentUrl.slice(0, currentUrl.indexOf('#'));
    const hashPath = currentUrl.slice(currentUrl.indexOf('#') + 1);
    const serviceUrl = `http://home.ustc.edu.cn/~jarvis/cas/index.html?r=${new Date().getTime()}`;
    if (currentUrl.includes('ticket')) {
      const ticket = currentUrl.match(/ticket=([\s\S]+?)&/)[1];
      const service = currentUrl.match(/service=([\s\S]+?)&/)[1];
      const hashpath = currentUrl.match(/hashpath=([\s\S]+)#\//)[1];
      axios.get(`/api/v1/token?id=null&ticket=${ticket}&service=${service}`)
        .then((res) => {
          if (res.status === 200) {
            if (hashpath.includes('/admin')) {
              this.$store.commit('setAdminAdminToken', res.data.access_token);
            } else {
              this.$store.commit('setAdminTeacherToken', res.data.access_token);
            }
            window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}#${hashpath}`;
          }
        });
    } else if ((hashPath.includes('/admin') && !this.$store.state.adminAdminToken)
      || (hashPath.includes('/teacher') && !this.$store.state.adminTeacherToken)) {
      const url = `${serviceUrl}${encodeURIComponent(`&apppath=${appPath}&hashpath=${hashPath}`)}`;
      const casUrl = `http://passport.ustc.edu.cn/login?service=${encodeURIComponent(url)}`;
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
