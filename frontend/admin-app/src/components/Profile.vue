<template>
  <div>
    <el-dialog
      title='个人资料' @close="handleCancel"
      :visible.sync="visible" :dialogVisible="dialogVisible"
      width="720px">
      <el-row type="flex" justify="center">
        <el-col :span="20">
          <el-form label-position="left" label-width="140px"
            :model="form" :rules="rules" ref="form">
            <el-form-item label="学号">
              <el-input v-model="form.id" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="姓名">
              <el-input v-model="form.name" :disabled="true"></el-input>
            </el-form-item>
            <el-form-item label="昵称" prop="nickname">
              <el-input v-model="form.nickname"></el-input>
            </el-form-item>
            <el-form-item label="邮箱" prop="email">
              <el-input v-model="form.email"></el-input>
            </el-form-item>
            <el-form-item label="电话" prop="phone">
              <el-input v-model="form.phone"></el-input>
            </el-form-item>
            <el-form-item label="学院">
              <el-input v-model="form.school" :disabled="true"></el-input>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <span slot="footer" class="dialog-footer">
        <el-button @click="handleCancel">取 消</el-button>
        <el-button type="primary" @click="submit(form.id)">确 定</el-button>
      </span>
  </el-dialog>
  </div>
</template>

<script>
import axios from 'axios';

export function isPhone(rule, value, callback) {
  const reg = /^[1][3,4,5,7,8][0-9]{9}$/;
  if (value === '' || value === undefined || value === null) {
    callback();
  } else if ((!reg.test(value)) && value !== '') {
    console.log('invalid phone!');
    callback(new Error('请输入正确的电话号码'));
  } else {
    callback();
  }
}
export function isEmail(rule, value, callback) {
  const reg = /^([a-zA-Z0-9]+[-_.]?)+@[a-zA-Z0-9]+\.[a-z]+$/;
  if (value === '' || value === undefined || value == null) {
    callback();
  } else if (!reg.test(value)) {
    console.log('invalid email!');
    callback(new Error('请输入正确的邮箱地址'));
  } else {
    callback();
  }
}
export default {
  name: 'Profile',
  props: {
    dialogVisible: {
      type: Boolean,
      default: false,
    },
    id: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      visible: false,
      form: {
        id: '',
        name: '',
        nickname: '',
        email: '',
        phone: '',
        school: '',
      },
      rules: {
        nickname: [
          { required: true, message: '请输入昵称', trigger: ['change', 'blur'] },
        ],
        email: [
          {
            validator: isEmail, required: true, message: '请输入正确的邮箱', trigger: ['change', 'blur'],
          },
        ],
        phone: [
          { validator: isPhone, message: '请输入正确的联系电话', trigger: ['change', 'blur'] },
        ],
      },
    };
  },
  watch: {
    dialogVisible() {
      this.visible = this.dialogVisible;
    },
  },
  mounted() {
    console.log(this.id);
    this.form.id = this.id;
    axios.get(`/api/v1/users/${this.id}`).then((res) => {
      console.log(res);
      if (res.status === 200) {
        this.form.nickname = res.data.nickname;
        this.form.email = res.data.email;
        this.form.phone = res.data.phone;
      }
    });
  },
  methods: {
    handleCancel() {
      this.$emit('update:dialogVisible', false);
    },
    submit(id) {
      this.$refs.form.validate((valid) => {
        if (!valid) {
          this.$message.error('请正确填写完表格再提交！');
          return;
        }
        axios.put(`/api/v1/users/${id}`, {
          id: this.form.id,
          name: this.form.name,
          nickname: this.form.nickname,
          email: this.form.email,
          phone: this.form.phone,
          school: this.form.school,
        });
        console.log(id);
        this.$emit('update:dialogVisible', false);
      });
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
