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
              您的身份是{{ $store.state.auth }}，您无权访问{{ systemName }}后台管理系统！
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
  name: 'LoginView',
  mounted() {
    console.log(this.$store.state.gid);
    if (this.$store.state.gid) {
      if (this.$route.path.includes('teacher')
      && this.$store.state.auth === '教师') {
        this.$router.push({
          path: '/teacher',
          name: 'TeacherView',
          params: {
            tid: this.$store.state.gid,
          },
        });
      } else if (this.$store.state.auth === '管理员') {
        this.$router.push({
          path: '/admin',
          name: 'AdminView',
          params: {
            aid: this.$store.state.gid,
          },
        });
      }
    }
  },
  computed: {
    systemName() {
      if (this.$route.path.includes('teacher')) {
        return '教师/助教';
      }
      return '管理员';
    },
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
        const hashparam = 'teacher/';
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
