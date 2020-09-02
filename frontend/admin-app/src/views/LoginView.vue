<template>
  <div>
    <span>您的身份是{{ $store.state.auth }}，您无权访问管理系统!</span>
    <button @click="commandHandler('logout')">点击登出</button>
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
  methods: {
    commandHandler(command) {
      if (command === 'logout') {
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
      } else if (command === 'profile') {
        this.dialogVisible = true;
      }
    },
  },
};
</script>

<style scoped>
</style>
