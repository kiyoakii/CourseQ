<template>
  <div>
    <span>您无权访问管理系统</span>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  mounted() {
    console.log(this.$store.state.gid);
    if (this.$store.state.gid) {
      if (this.$route.path.includes('teacher')) {
        this.$router.push({
          path: '/teacher/',
          name: 'TeacherView',
          params: {
            tid: this.$store.state.gid,
          },
        });
      } else {
        this.$router.push({
          path: '/admin/',
          name: 'AdminView',
          params: {
            aid: this.$store.state.gid,
          },
        });
      }
    }
  },
};
</script>

<style scoped>
</style>
