<template>
  <div class="user-profile">
    <el-row type="flex" justify="center" align="middle" class="h-100"
      :style="{ backgroundImage: 'url(' + require('@/assets/imgs/login-bg.jpg') + ')' }">
      <el-card class="box-card form-card">
        <div slot="header" class="clearfix">
          <span>提示</span>
        </div>
        <div class="content">
            <el-row class="text-content">
              您不属于该课程，无权访问该答疑系统！<br><br>
              请检查您输入的网址或您登录的账号。
            </el-row>
            <el-row type="flex" justify="center">
              <el-button type="primary" @click="onLogout">点击登出</el-button>
            </el-row>
        </div>
      </el-card>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'UnAuthView',
  mounted() {
    alert(this.$route.path);
    this.axios.get(`/api/v1/courses/${this.$route.params.cid}/questions`, {
      headers: {
        Authorization: `Bearer ${this.$store.state.proansToken}`,
      },
    }).then((res) => {
      if (res.status === 200) {
        this.$store.commit('initProblems', res.data);
        this.$router.push({
          name: 'IntroView',
        });
      }
    }).catch((err) => {
      console.log(err.response);
    });
  },
  methods: {
    onLogout() {
      this.$confirm('确认登出, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning',
      }).then(() => {
        this.$message({
          type: 'success',
          message: '登出成功!',
        });
        this.$store.commit('setToken', '');
        const currentUrl = window.location.href;
        const appname = currentUrl.slice(0, currentUrl.indexOf('#'));
        // const hashparam = currentUrl.match(/\/teacher\/\d*\//g);
        const hashparam = `proans/course/${this.$route.params.cid}`;
        const serviceUrl = `${appname}?hashparam=${hashparam}`;
        window.location.href = `http://passport.ustc.edu.cn/logout?service=${encodeURIComponent(serviceUrl)}`;
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消登出',
        });
      });
    },
  },
};
</script>

<style scoped>
.user-profile {
  width: 100%;
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.text-content {
  margin-bottom: 20px;
}

.w-100 {
  width: 100%;
}

.h-100 {
  height: 100vh;
}

.form-card {
  width: 400px;
  margin-bottom: 100px;
  background-color: rgba(255, 255, 255, 0.85) !important;
  /* height: 400px; */
}
</style>
