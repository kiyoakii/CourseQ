<template>
  <div class="user-profile-steps">
    <el-row type="flex" justify="center" align="middle" class="h-100"
      :style="{ backgroundImage: 'url(' + require('@/assets/imgs/login-bg.jpg') + ')' }">
      <el-card class="box-card form-card">
        <div slot="header" class="clearfix">
          <span>完善用户信息</span>
        </div>
        <div class="content">
          <el-form :rules="rules" ref="form"
            :model="profile" label-width="60px" label-position="right">
            <el-form-item label="姓名" prop="name">
              <el-input v-model="profile.name"></el-input>
            </el-form-item>
            <el-form-item label="昵称" prop="nickname">
              <el-input v-model="profile.nickname"></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="profile.email"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="phone">
              <el-input v-model="profile.phone"></el-input>
            </el-form-item>
            <el-row type="flex" justify="center">
              <el-button type="primary" @click="onSubmit">确认</el-button>
            </el-row>
          </el-form>
        </div>
      </el-card>
    </el-row>
    <el-dialog
      title="提示"
      :visible.sync="dialogVisible"
      width="30%"
      >
      <span>激活链接已经发送到你的邮箱，请注意及时查收和激活。</span>
      <span slot="footer" class="dialog-footer">
        <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'UserProfileSteps',
  props: {
    token: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      currentStep: 1,
      dialogVisible: false,
      profile: {
        nickname: '',
        email: '',
        phone: '',
      },
      rules: {
        name: [
          { required: true, message: '请输入姓名', trigger: ['blur'] },
        ],
        nickname: [
          { required: true, message: '请输入昵称', trigger: ['blur'] },
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: ['blur'] },
          {
            type: 'email',
            message: '请输入正确的邮箱地址',
            trigger: ['blur', 'change'],
          },
        ],
      },
    };
  },
  methods: {
    onSubmit() {
      console.log(this.token);
      this.axios({
        method: 'post',
        url: '/api/v1/users/register',
        data: {
          ...this.profile,
          redirect_path: `/proans/course/${this.$store.state.cid}`,
        },
        headers: {
          Authorization: `Bearer ${this.token}`,
        },
      }).then((res) => {
        if (res.status === 200) {
          this.dialogVisible = true;
          // this.$emit('submit', {
          //   showUserProfileSteps: false,
          //   data: res.data,
          // });
        }
      });
    },
  },
};
</script>

<style scoped>


.user-profile-steps {
  width: 100%;
  height: 100vh;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
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

.mb-4 {
  padding-bottom: 50px;
}
</style>
