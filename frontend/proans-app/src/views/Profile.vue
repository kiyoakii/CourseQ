<template>
  <div>
    <!-- This is Profile view. -->
    <el-header>
      <div class="header">
        <router-link to="/">
          <el-button type="primary" plain>答疑平台</el-button>
        </router-link>
      </div>
      <el-avatar :src="img"></el-avatar>
    </el-header>
    <el-main>
      <el-row type="flex" justify="center">
        <el-col :span="8" type="flex" justify="center">
          <el-row>
            <div>
              <div class="block">
                <el-avatar :size="200" :src="img"></el-avatar>
              </div>
            </div>
          </el-row>
          <el-row class="photo-change">
            <el-upload
              class="upload-demo"
              action="https://jsonplaceholder.typicode.com/posts/"
              :show-file-list="false"
              :on-success="handleAvatarSuccess"
              :before-upload="beforeAvatarUpload"
              :file-list="fileList">
              <el-button>更换头像</el-button>
            </el-upload>
          </el-row>
        </el-col>
        <el-col :span="14" class="name">
          <el-row>
            <el-col :span="6">
              <h2>{{name}}</h2>
            </el-col>
            <el-col :span="4">
              <el-button>修改密码</el-button>
            </el-col>
            <el-col :span="4">
              <el-button>修改个人信息</el-button>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
      <el-row>
        <el-card class="info">
          <div slot="header">
            <h3>个人信息</h3>
          </div>
          {{info}}
        </el-card>
      </el-row>
    </el-main>
  </div>
</template>

<script>
export default {
  name: 'Profile',
  data() {
    return {
      name: '学生姓名',
      info: '个人信息',
      img: 'https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png',
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      this.img = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === 'image/jpeg';
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!');
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!');
      }
      return isJPG && isLt2M;
    },
  },
};
</script>

<style scoped>
.el-header {
  /* padding: 0 !important; */
  border-bottom: 1px solid #eeeeee;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  display: flex;
  /* align-items:center; */
  /* justify-content:center; */
}
.header {
  margin: 10px 30px;
}
.el-avatar {
  margin-left: auto;
  margin-right: 30px;
  margin-top: 10px
}
.photo-change {
  display: flex;
  padding: 0 60px;
}
.name {
  flex-direction: column;
  display:flex;
  justify-content: center;
}
.info {
  margin: 30px 0;
}
</style>
