<template>
  <div id="app">
    <el-container v-show="showUserProfileSteps" style="height: 100vh;">
      <user-profile-steps
        :token='token'
        @submit="change">
      </user-profile-steps>
    </el-container>
    <el-container v-show="!showUserProfileSteps">
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
import axios from 'axios';
import UserProfileSteps from './components/UserProfileSteps.vue';

export default {
  name: 'app',
  components: {
    VueHeader,
    UserProfileSteps,
    VueContent,
  },
  data() {
    return {
      showUserProfileSteps: false,
      token: '',
    };
  },
  methods: {
    change(options) {
      this.showUserProfileSteps = options.showUserProfileSteps || false;
      const data = options.data;
      console.log(data);
      this.$store.commit('setGid', data.gid);
      this.$store.commit('setProansToken', data.access_token);
      const currentUrl = window.location.href;
      const hashpath = currentUrl.match(/hashpath=([\s\S]+)#\//)[1];
      window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}#${hashpath}`;
    },
  },
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
      // const hashpath = currentUrl.match(/hashpath=([\s\S]+)#\//)[1];
      axios.get(`/api/v1/token?id=null&ticket=${ticket}&service=${service}`)
        .then((res) => {
          if (res.status === 200) {
            console.log('token res.data: ', res.data);
            this.token = res.data.access_token;
            if (res.data.registered) {
              this.$store.commit('setProansToken', res.data.access_token);
              this.$store.dispatch('initProblems');
              this.$store.commit('setGid', res.data.gid);
              window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}`;
              return;
            }
            this.showUserProfileSteps = true;
            // window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}#${hashpath}`;
            // window.location.href = `${currentUrl.slice(0, currentUrl.indexOf('?'))}`;
          }
        }).catch((e) => {
          console.log(e);
        });
    } else if (!this.$store.state.proansToken) {
      const url = `${serviceUrl}${encodeURIComponent(`&apppath=${appPath}&hashpath=${hashPath}`)}`;
      const casUrl = `http://passport.ustc.edu.cn/login?service=${encodeURIComponent(url)}`;
      window.location.href = casUrl;
    }
  },
};
</script>

<style scoped>
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
