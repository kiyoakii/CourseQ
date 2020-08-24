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
export default {
  name: 'Profile',
  props: {
    dialogVisible: {
      type: Boolean,
      default: false,
    },
    id: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      visible: false,
      form: {
        id: 123,
        name: '123',
        nickname: '1234',
        email: '123@',
        phone: '112',
        school: '12',
      },
      rules: {
        nickname: [
          { required: true, message: '请输入昵称', trigger: ['change', 'blur'] },
        ],
        email: [
          { required: true, message: '请输入邮箱', trigger: ['change', 'blur'] },
        ],
        phone: [
          { message: '请输入联系电话', trigger: ['change', 'blur'] },
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
