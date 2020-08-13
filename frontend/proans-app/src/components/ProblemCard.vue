<template>
  <div>
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span class="title">{{ problem.title }}</span>
        <span class="tags" v-for="tag in problem.tags" :key="tag.id">
          <el-tag class="success" size="mini">{{ tag.name }}</el-tag>
        </span>
        <div class="stars">
          <img src="../assets/star-off.png" class="star">
          <span >{{ problem.stars }}</span>
          <i class="el-icon-star-off star"></i>
        </div>
      </div>
      <div class="text item">
        {{ problem.content }}
      </div>
      <div class="footer">
        <div class="edit-info">
          <span>{{ problem.author.nickname }} 于
            {{ (new Date(problem.update_datetime))
            .toLocaleString('zh-CN', { timeZone: 'UTC'}) }} 修改</span>
        </div>
        <div class="buttons">
          <el-button size="medium"
          @click="dialogFormVisible = true">编辑</el-button>
          <el-popover
          placement="top"
          width="160"
          v-model="popoverVisible">
          <p>确定删除吗？</p>
          <div style="text-align: right; margin: 0">
            <el-button size="mini" type="text" @click="popoverVisible = false">取消</el-button>
            <el-button type="primary" size="mini" @click="handleDelete">确定</el-button>
          </div>
          <el-button slot="reference">删除</el-button>
        </el-popover>
        </div>
      </div>
    </el-card>
    <el-dialog title="编辑问题描述" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="标题" :label-width="formLabelWidth">
          <el-input v-model="form.title" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="问题描述" :label-width="formLabelWidth">
          <el-input v-model="form.content" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>

export default {
  name: 'ProblemCard',
  props: {
    problem: {
      type: Object,
      default() {
        return {
          title: '',
          tags: [],
          content: '',
        };
      },
    },
  },
  data() {
    return {
      dialogFormVisible: false,
      form: {
        title: '',
        content: '',
      },
      formLabelWidth: '120px',
      popoverVisible: false,
    };
  },
  methods: {
    handleDelete() {
      // this.axios.delete(`/api/v1/questions/${this.problem.id}`)
      //   .then((res) => {
      //     console.log(res);
      //     this.popoverVisible = false;
      //     if (res.status !== 200) {
      //       console.log(JSON.stringify(res.data));
      //     }
      //   });
      console.log((new Date(this.problem.update_datetime)).toLocaleString());
    },
  },
};
</script>

<style scoped>
.tags {
  margin-left: 10px;
}
.el-tag {
  font-size: 10px;
}
.title {
  font-size: 18px;
}
.footer {
  padding-top: 20px;
  display: flex;
  justify-content:space-between;
  align-items: flex-end;
}
.stars {
  float: right;
  font-size: 16px;
  display: flex;
  align-items: center;
}
.edit-info {
  font-size: 12px;
  color: #606266;
}
.star {
  width: 20px;
  margin-right: 5px;
  margin-left: 20px;
}
</style>
