<template>
  <div>
    <!-- This is the SignIn view. -->
    <el-form ref="loginForm" :model="form" :rules="rules" status-icon
      label-width="80px" class="login-box">
      <h3 class="title">答疑平台登录</h3>
      <el-form-item label="用户名" prop="username">
        <el-input type="text" v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码" prop="password" class="pwd-input">
        <el-input type="text" v-model="form.password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <div class="pwd-forget">
        <el-link href="https://element.eleme.io" type="info" class="forget-link">忘记密码?</el-link>
      </div>
      <div class="signin-btn">
        <el-button type="primary" v-on:click="onSubmit('loginForm')">
          登录
        </el-button>
      </div>
    </el-form>
    <el-dialog
      title="温馨提示" :visible.sync="dialogVisible" width="30%" :before-close="handleClose">
      <span>请输入用户名和密码</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'SignIn',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
      rules: {
        username: [
          { required: true, message: '用户名不可为空', trigger: 'blur' },
        ],
        password: [
          { required: true, message: '密码不可为空', trigger: 'blur' },
        ],
      },
      dialogVisible: false,
    };
  },
  methods: {
    onSubmit(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$router.push('/');
        } else {
          this.dialogVisible = true;
          return false;
        }
        return true;
      });
    },
  },
};
</script>

<style scoped>
.login-box {
  border: 1px solid #DCDFE6;
  width: 350px;
  margin: 150px auto;
  padding: 35px 35px 15px 35px;
  border-radius: 5px;
  box-shadow: 0 0 5px #909399;
  }
.title {
  text-align: center;
  margin: 0 auto 40px auto;
  color: #303133;
}
.pwd-input {
  margin-bottom: 0;
}
.forget-link {
  margin-left: auto;
  margin-bottom: 22px;
  color: #909399;
}
.signin-btn {
  display: flex;
  justify-content: center;
  margin-bottom: 22px;
}
.pwd-forget {
  display: flex;
  align-items: center;
}
</style>
