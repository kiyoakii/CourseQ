<template>
  <el-row class="header">
    <el-col :span="1">
      <el-button icon="el-icon-s-home"
        @click="handleRet" class="btn-back" circle
        :class="(activeHome) ? 'folder-opened' : 'folder-closed'"> </el-button>
    </el-col>
    <el-col :span="19" class="tags-list">
      <problem-categories></problem-categories>
    </el-col>
    <el-col :span="4">
      <el-row type="flex" justify="space-around">
        <el-button @click="myLike()">我的点赞</el-button>
        <el-dropdown placement="bottom" @command="commandHandler" size="medium">
          <el-avatar src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"></el-avatar>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="profile">个人资料</el-dropdown-item>
            <el-dropdown-item command="logout">登出</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-row>
    </el-col>
    <profile :dialogVisible.sync="dialogVisible" :id="this.$store.state.gid"></profile>
  </el-row>
</template>

<script>
import ProblemCategories from '@/components/ProblemCategories.vue';
import Profile from '@/components/Profile.vue';

export default {
  name: 'VueHeader',
  components: {
    ProblemCategories,
    Profile,
  },
  data() {
    return {
      dialogVisible: false,
    };
  },
  methods: {
    myLike() {
      if (this.$route.params.tid !== '0') {
        this.$router.push({
          path: `/proans/course/${this.$route.params.cid}/tag/0`,
        });
      }
    },
    handleRet() {
      this.$router.push({
        path: `/proans/course/${this.$route.params.cid}`,
      });
    },
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
          this.$store.commit('setProansToken', '');
          // window.location.reload();
          const currentUrl = window.location.href;
          const appname = currentUrl.slice(0, currentUrl.indexOf('#'));
          const hashparam = currentUrl.slice(currentUrl.indexOf('#') + 1);
          const serviceUrl = `${appname}?hashparam=${hashparam}`;
          window.location.href = `http://passport.ustc.edu.cn/logout?service=${encodeURIComponent(serviceUrl)}`;
          // window.location.href = `http://passport.ustc.edu.cn/logout?service=${encodeURIComponent(serviceUrl)}`;
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
  computed: {
    activeHome() {
      return this.$route.params.tid === 'all';
    },
  },
};
</script>

<style scoped>
.header {
  height: 100%;
  display: flex;
  align-items: center;
}

.tags-list {
  height: 100%;
}

.btn-back {
  margin-left: 25px;
}

.folder-opened  {
  background-color: #ecf5ff;
  color: #409eff;
}
</style>
