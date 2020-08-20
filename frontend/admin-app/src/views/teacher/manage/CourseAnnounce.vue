<template>
  <div class="course-announce">
    <div class="header">
      <h2 id="title">课程公告</h2>
    </div>
    <div class="btn-header">
      <el-button type="primary"
      @click="handleCreate">新建公告</el-button>
    </div>
    <el-row class="announce" v-for="anno in allInfo.announces" :key="anno.id">
      <el-card class="card-box" shadow="hover">
        <div slot="header" class="clearfix card-header">
          <span>{{ anno.title }}</span>
          <div>
            <el-button type="primary"
            icon="el-icon-edit" size="small"
            @click="handleEdit(anno)">编辑</el-button>
            <el-button type="danger"
            icon="el-icon-delete" size="small"
            @click="handleDelete(anno.id)">删除</el-button>
          </div>
        </div>
        <div class="text-wrapper">
          {{ anno.content }}
        </div>
      </el-card>
    </el-row>
    <el-dialog
      :title="form.id === '' ? '添加' : '编辑'"
      :visible.sync="dialogVisible"
      width="720px">
      <el-form :model="form">
        <el-form-item label="标题" >
          <el-input v-model="form.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="内容" >
          <el-input v-model="form.content"
          type="textarea"
          :autosize="{ minRows: 4}"
          placeholder="请输入内容"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit(form.id)">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  props: {
    allInfo: {},
  },
  data() {
    return {
      dialogVisible: false,
      form: {
        id: '',
        title: '',
        content: '',
      },
    };
  },
  methods: {
    handleCreate() {
      this.form = {
        id: '',
        title: '',
        content: '',
      };
      this.dialogVisible = true;
    },
    submit(id) {
      const url = id === ''
        ? `/api/v1/courses/${this.$route.params.cid}/announces` : `/api/v1/announces/${id}`;
      const method = id === '' ? 'post' : 'put';
      this.axios({
        url,
        method,
        data: {
          ...this.form,
        },
      }).then((res) => {
        if (res.status !== 200) {
          return;
        }
        this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
      }).catch((err) => {
        console.log(err);
      });
      this.dialogVisible = false;
    },
    handleEdit(anno) {
      this.form = {
        id: anno.id,
        title: anno.title,
        content: anno.content,
      };
      this.dialogVisible = true;
    },
    handleDelete(aid) {
      this.axios.delete(`/api/v1/announces/${aid}`,
        this.form)
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
    },
  },
};
</script>

<style scoped>
.announce {
  margin-bottom: 15px;
}
.card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.course-announce {
  width:880px;
}

.header {
  display:flex;
  flex-direction: row;
  justify-content: space-between;
}

.text-wrapper {
  white-space: pre-wrap;
}

.btn-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}
#title {
  margin-top: 20px;
}
</style>
