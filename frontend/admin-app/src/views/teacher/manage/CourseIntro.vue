<template>
  <div class="intro">
    <h2 id="title">课程简介</h2>
    <div class="btn-header">
      <el-button type="primary"
      @click="handleEdit">编辑简介</el-button>
    </div>
    <el-card class="box-card" shadow="none">
      <div slot="header" class="clearfix">
        <span class="title">{{ allInfo.name_zh }}</span>
        <span class="subtitle"> {{ allInfo.name_en }}</span>
        <div class="footer">
          {{ allInfo.semester }}
        </div>
      </div>
      <div class="text-wrapper item">
        {{ allInfo.intro }}
      </div>
    </el-card>
    <el-card class="message-card" shadow="none">
      <el-row>
        <div class="text-wrapper item">
          <span class="subtitle">教师：</span>
          <span v-for="teacher in allInfo.teachers" :key="teacher.gid">
            {{ teacher.name }}
          </span>
        </div>
      </el-row>
      <el-row>
        <div class="text-wrapper item">
          <span class="subtitle">预修课程：</span>
          <span>{{allInfo.pre_course}}</span>
        </div>
      </el-row>
      <el-row>
        <div class="text-wrapper item">
          <span class="subtitle">参考教材：</span>
          <span>{{allInfo.textbooks}}</span>
        </div>
      </el-row>
    </el-card>
    <el-dialog
      :title="'添加'"
      :visible.sync="dialogVisible"
      width="720px">
     <el-form :model="form">
        <el-form-item label="中文名" >
          <el-input v-model="form.name_zh" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="英文名" >
          <el-input v-model="form.name_en" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="学期" >
          <el-input v-model="form.semester" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="简介" >
          <el-input v-model="form.intro"
          type="textarea"
          :autosize="{ minRows: 4}"
          placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="预修课程" >
          <el-input v-model="form.preCourse" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="参考教材" >
          <el-input v-model="form.textbooks" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="submit">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'CourseIntro',
  props: {
    allInfo: {},
  },
  data() {
    return {
      form: {
        name_zh: '',
        name_en: '',
        semester: '',
        intro: '',
        preCourse: '',
        textbooks: '',
      },
      dialogVisible: false,
    };
  },
  methods: {
    handleEdit() {
      this.form = {
        name_zh: this.allInfo.name_zh,
        name_en: this.allInfo.name_en,
        semester: this.allInfo.semester,
        intro: this.allInfo.intro,
        preCourse: this.allInfo.pre_course,
        textbooks: this.allInfo.textbooks,
      };
      this.dialogVisible = true;
    },
    submit() {
      const data = {
        name_zh: this.form.name_zh,
        name_en: this.form.name_en,
        intro: this.form.intro,
        series: this.allInfo.series,
        pre_course: this.form.preCourse,
        textbooks: this.form.textbooks,
        semester: this.form.semester,
        new_teachers_gid: [],
        new_students_gid: [],
        new_TAs_gid: [],
        del_teachers_gid: [],
        del_students_gid: [],
        del_TAs_gid: [],
      };
      this.axios.patch(`/api/v1/courses/${this.$route.params.cid}`,
        data)
        .then((res) => {
          console.log(res);
          this.dialogVisible = false;
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
    },
  },
};
</script>

<style>
#title {
  margin-top: 20px;
}
.tags {
  margin-left: 10px;
}
.el-tag {
  font-size: 10px;
}
.title {
  font-size: 30px;
}
.subtitle {
  font-size: 22px;
}
.footer {
  padding-top: 20px;
  display: flex;
  justify-content: flex-end;
}
.intro {
  width:900px;
}
.message-card {
  margin-top: 50px;
}

.text-wrapper {
  white-space: pre-wrap;
}

.btn-header {
  display: flex;
  justify-content: flex-end;
  margin-bottom: 20px;
}
</style>
