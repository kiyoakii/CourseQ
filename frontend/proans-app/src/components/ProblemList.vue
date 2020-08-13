<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in problems" :key="index " class="infinite-list-item"
        @click="getProblem(problem.id)" >
        <el-card class="box-card" shadow="hover"
        :class="{selected:selectedProblem === problem.id}">
          <div slot="header" class="clearfix">
            <span>{{ problem.title }}</span>
          </div>
          <div class="text item">
            {{ problem.content | formatDesc }}
          </div>
        </el-card>
      </li>
      <li @click="dialogFormVisible = true">
        <el-card class="box-card center" shadow="hover">
          <img src="@/assets/add.png" class="add-img">
        </el-card>
      </li>
    </ul>
    <el-dialog title="新建问题" :visible.sync="dialogFormVisible">
      <div class="editor">
        <div class="title">
          <el-input placeholder="主题"
          v-model="form.title"></el-input>
        </div>
        <el-tag
          :key="tag"
          v-for="tag in form.tags"
          closable
          :disable-transitions="false"
          @close="handleClose(tag)">
          {{tag}}
        </el-tag>
        <el-input
          class="input-new-tag"
          v-if="inputVisible"
          v-model="inputValue"
          ref="saveTagInput"
          size="small"
          @keyup.enter.native="handleInputConfirm"
          @blur="handleInputConfirm"
        >
        </el-input>
        <el-button v-else class="button-new-tag" size="small"
        @click="showInput">+ New Tag</el-button>
        <mavon-editor class="mavon-editor" v-model="form.content"></mavon-editor>
      </div>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'ProblemList',
  props: {
    problems: Array,
  },
  data() {
    return {
      count: 0,
      selectedProblem: -1,
      dialogFormVisible: false,
      form: {
        title: '',
        content: '',
        tags: ['标签1'],
      },
      formLabelWidth: '120px',
      inputVisible: false,
      inputValue: '',
    };
  },
  methods: {
    load() {
      this.count += 2;
    },
    getProblem(proid) {
      this.selectedProblem = proid;
      this.$router.push({
        path: '/proans/',
        name: 'CategoryView',
        query: {
          tid: this.$route.query.tid,
          qid: proid,
        },
      });
    },
    handleClose(tag) {
      this.form.tags.splice(this.form.tags.indexOf(tag), 1);
    },
    showInput() {
      this.inputVisible = true;
      this.$nextTick((_) => {
        console.log(_);
        this.$refs.saveTagInput.$refs.input.focus();
      });
    },
    handleInputConfirm() {
      if (this.inputValue) {
        this.form.tags.push(this.inputValue);
      }
      this.inputVisible = false;
      this.inputValue = '';
    },
    onSubmit() {
      this.axios.post('/api/v1/courses/3/questions',
        this.form)
        .then((res) => {
          console.log(res);
          if (res.status !== 200) {
            console.log(JSON.stringify(res.data));
            return;
          }
          console.log('成功');
          this.dialogFormVisible = false;
        });
    },
  },
  filters: {
    formatDesc(value) {
      return value.length <= 50 ? value : `${value.slice(0, 50)}...`;
    },
  },
};
</script>

<style scoped>
.box-card {
  font-weight: 600;
  margin-bottom: 15px;
  cursor: pointer;
}

.box-card:hover {
  background: rgba(250, 250, 250, .8);
}

.text {
  font-size: 12px;
}

.link {
  text-decoration: none;
  color: #303133;
  display: block;
}
.selected {
  background-color: #ecf5ff;
}
.center {
  display: flex;
  justify-content: center;
}
.add-img {
  width: 40px;
}
.el-tag + .el-tag {
    margin-left: 10px;
  }
  .button-new-tag {
    margin-left: 10px;
    height: 32px;
    line-height: 30px;
    padding-top: 0;
    padding-bottom: 0;
  }
  .input-new-tag {
    width: 90px;
    margin-left: 10px;
    vertical-align: bottom;
  }

.title {
  margin: 10px 0;
}
.mavon-editor {
  margin: 20px 0;
}
</style>
