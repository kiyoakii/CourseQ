<template>
  <div id="app">
    <el-container v-show="showUserProfile" style="height: 100vh;">
      <user-profile
        :token='token'
        @submit="change">
      </user-profile>
    </el-container>
    <router-view v-show="!showUserProfile"></router-view>
  </div>
</template>

<script>
import axios from 'axios';
import UserProfile from './components/UserProfile.vue';

export default {
  name: 'app',
  components: {
    UserProfile,
  },
  data() {
    return {
      showUserProfile: false,
      token: '',
      loadingInstance: {},
    };
  },
  methods: {
    change(options) {
      this.showUserProfile = options.showUserProfile || false;
      const { data } = options;
      console.log(data);
      const currentUrl = window.location.href;
      const hashpath = currentUrl.match(/hashpath=([\s\S]+)#\//)[1];
      this.$store.commit('setToken', data.access_token);
      this.$store.commit('setGid', data.gid);
      window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}#${hashpath}`;
    },
  },
  created() {
    this.loadingInstance = this.$loading({
      fullscreen: true,
    });
  },
  beforeMount() {
    this.loadingInstance.close();
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
      // const hashpath = currentUrl.match(/hashpath=([\s\S]+)#\//)[1];
      axios.get(`/api/v1/token?id=null&ticket=${ticket}&service=${service}`)
      // axios.get('/api/v1/token/0000000000') // test
        .then((res) => {
          console.log(res);
          if (res.status === 200) {
            this.token = res.data.access_token;
            if (res.data.registered) {
              this.$store.commit('setToken', res.data.access_token);
              this.$store.commit('setGid', res.data.gid);
              // window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}`;
              if (currentUrl.includes('teacher')) {
                window.location.href = `${appPath}#/teacher/${res.data.gid}`;
              } else {
                window.location.href = `${appPath}#/admin/${res.data.gid}`;
              }
              return;
            }
            this.showUserProfile = true;
          }
        });
    } else if (!this.$store.state.token) {
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
