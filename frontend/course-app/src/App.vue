<template>
  <div id="app">
    <el-container>
      <el-header >
        <vue-header :allinfo="allinfo"></vue-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-col :xs="24" :sm="24" :md="22" :lg="18" :xl="18" >
            <vue-content :allinfo="allinfo"></vue-content>
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
  data() {
    return {
      allinfo: {},
    };
  },
  mounted() {
    this.updateAllInfo();
  },
  watch: {
    $route() {
      this.updateAllInfo();
    },
  },
  methods: {
    updateAllInfo() {
      this.axios.get(`/api/v1/courses/${this.$route.params.cid}`)
        .then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
            return;
          }
          this.allinfo = res.data;
        });
    },
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
}
</style>
