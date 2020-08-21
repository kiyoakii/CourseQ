<template>
  <div>
    <h2 id="title">日程安排</h2>
    <div class="schedule">
      <el-table :data="schedules"
        border
        :header-cell-style="{'text-align':'center'}"
        highlight-current-row>
        <el-scrollbar>
          <el-table-column prop="week" label="教学周"
            width="70"
            align="center"
            fixed
            style="font-weight:bold"></el-table-column>
          <el-table-column label="课程"
            align="left" :show-overflow-tooltip="true">
            <el-table-column v-for="i in maxLecsNum" :key="i" :label="`Lec${i}`"
            align="left" :show-overflow-tooltip="true">
              <el-table-column label="主题"
              width="120"
              align="center">
                <template slot-scope="scope">
                  <el-tooltip class="item" effect="dark" content="点击修改该日程" placement="top">
                    <div>
                      <el-row>
                        <span class="click-area" @click="handleEdit(scope.row.lectures[i-1])">
                        {{ scope.row.lectures.length >= i
                        ? scope.row.lectures[i - 1].topic : '' }}
                        </span>
                      </el-row>
                      <el-row>
                        <span class="click-area light-text"
                        @click="handleEdit(scope.row.lectures[i-1])"
                        >
                          {{ scope.row.lectures.length >= i
                        ? `参考章节：${scope.row.lectures[i - 1].reference}` : '' }}</span>
                      </el-row>
                    </div>
                  </el-tooltip>
                </template>
              </el-table-column>
              <el-table-column label="教学资源"
              min-width="120"
              align="center">
                <template slot-scope="scope">
                  <el-row v-for="(res, index) in
                  scope.row.lectures.length >= i
                  ? scope.row.lectures[i - 1].resources : []" :key="index">
                      <el-row>
                        <span>{{ res.description }}</span>
                      </el-row>
                      <el-row>
                        <el-link type="primary" :href="res.url">
                          {{ thumbnailFilename(res.filename) }}
                        </el-link>
                      </el-row>
                  </el-row>
                </template>
              </el-table-column>
              <el-table-column label="作业" min-width="120"
              align="center">
                <template slot-scope="scope">
                  <el-row v-for="(ass, index) in
                  scope.row.lectures.length >= i
                  ? scope.row.lectures[i - 1].assignments : []" :key="index"
                  :gutter="20">
                      <el-row>
                        <span>{{ ass.title }}</span>
                      </el-row>
                      <el-row>
                        <el-link type="primary" :href="ass.url">
                          {{ thumbnailFilename(ass.filename) }}</el-link>
                      </el-row>
                      <el-row class="light-text">
                        <span>ddl:{{ ass.due }}</span>
                      </el-row>
                  </el-row>
                </template>
              </el-table-column>
            </el-table-column>
          </el-table-column>
        </el-scrollbar>
      </el-table>
      <div class="btn-adder"
        @click="createSchedule">
        <i class="el-icon-plus"></i>
        <span>新增日程</span>
      </div>
      <!-- <el-button @click="deleteAssignment">delete</el-button> -->
      <el-dialog
        :title="isEdit ? '编辑' : '添加'"
        :visible.sync="dialogVisible"
        :before-close="handleClose"
        width="720px">
        <el-form :model="form">
          <el-form-item label="主题" >
            <el-input v-model="form.topic" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="参考章节" >
            <el-input v-model="form.reference" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="教学周" >
            <el-input v-model="form.week" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="教学资源" >
            <el-upload
              class="upload-demo"
              drag
              :headers="headers"
              action="eadf"
              :file-list="resFileList"
              :on-preview="handleResPreview"
              :on-remove="removeRes"
              :http-request="uploadRes"
              multiple>
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            </el-upload>
          </el-form-item>
          <el-form-item label="作业" >
            <el-upload
              class="upload-demo"
              drag
              :headers="headers"
              action="eadf"
              :file-list="assFileList"
              :on-preview="handleAssPreview"
              :on-remove="removeAss"
              :http-request="uploadAss"
              multiple>
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或<em>点击上传</em><br>
                点击文件添加描述
              </div>
            </el-upload>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button v-if="isEdit"
          type="danger"
          @click="deleteSchedule(form.id)">删 除</el-button>
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="submit">确 定</el-button>
        </span>
        <el-dialog
        :visible.sync="innerVisible"
        append-to-body>
          <el-form>
            <el-form-item :label="isRes ? '资源描述' : '作业描述'">
              <el-input v-if="isRes" v-model="form.description"
              placeholder="请输入资源描述"></el-input>
              <el-input v-else v-model="form.title"
              placeholder="请输入作业描述"></el-input>
            </el-form-item>
            <el-form-item v-if="!isRes"
            label="选择截止日期">
              <el-date-picker
                v-model="form.due"
                type="datetime"
                placeholder="选择日期时间"
                default-time="12:00:00">
              </el-date-picker>
            </el-form-item>
          </el-form>
          <span slot="footer" class="dialog-footer">
            <el-button @click="innerVisible = false">取 消</el-button>
            <el-button type="primary" @click="innerSubmit">确 定</el-button>
          </span>
        </el-dialog>
      </el-dialog>
    </div>
  </div>
</template>

<script>
import { schedulesFilter } from '@/helpers/filters';

export default {
  name: 'CourseSchedule',
  props: {
    allInfo: {},
  },
  data() {
    return {
      schedulesFilter,
      dialogVisible: false,
      innerVisible: false,
      isEdit: false,
      isRes: false,
      form: {
        topic: '',
        id: '',
        fileID: '',
        reference: '',
        week: '',
        description: '',
        title: '',
        due: '',
      },
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      resFileList: [],
      assFileList: [],
      fileToID: [],
      uploadResID: [],
      uploadAssID: [],
    };
  },
  methods: {
    deleteAssignment() {
      this.axios.delete('/api/v1/assignments/1')
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    innerSubmit() {
      let formData = new FormData();
      if (this.isRes) {
        formData.append('description', this.form.description);
        const url = `/api/v1/resources/${this.form.fileID}`;
        this.axios.patch(url,
          formData,
          {
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then((res) => {
            console.log(res);
            this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
          });
      } else {
        formData = new FormData();
        formData.append('title', this.form.title);
        formData.append('due', this.form.due.toISOString());
        const url = `/api/v1/assignments/${this.form.fileID}`;
        this.axios.patch(url,
          formData,
          {
            headers: { 'Content-Type': 'multipart/form-data' },
          })
          .then((res) => {
            console.log(res);
            this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
          });
      }
      this.innerVisible = false;
    },
    submit() {
      let option = {};
      if (this.isEdit) {
        option = {
          method: 'put',
          url: `/api/v1/schedules/${this.form.id}`,
        };
      } else {
        option = {
          method: 'post',
          url: `/api/v1/courses/${this.$route.params.cid}/schedules`,
        };
      }
      this.axios({
        ...option,
        data: {
          topic: this.form.topic,
          reference: this.form.reference,
          week: this.form.week,
          resource_ids: this.uploadResID,
          assignment_ids: this.uploadAssID,
        },
      })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
      this.dialogVisible = false;
    },
    handleEdit(lec) {
      console.log(lec);
      this.dialogVisible = true;
      this.isEdit = true;
      this.form = {
        topic: lec.topic,
        reference: lec.reference,
        week: lec.week,
        id: lec.id,
        description: '',
        title: lec.assignments.length > 0
          ? lec.assignments[0].title : '',
        due: lec.assignments.length > 0
          ? lec.assignments[0].due : '',
      };
      this.resFileList = [];
      this.assFileList = [];
      this.uploadResID = [];
      this.uploadAssID = [];
      lec.resources.forEach((item) => {
        this.resFileList.push({
          name: item.filename,
          url: item.url,
          id: item.id,
          description: item.description,
        });
        this.uploadResID.push(item.id);
      });
      lec.assignments.forEach((item) => {
        this.assFileList.push({
          name: item.filename,
          url: item.url,
          id: item.id,
          title: item.title,
          due: item.due,
        });
        this.uploadAssID.push(item.id);
      });
    },
    createSchedule() {
      this.dialogVisible = true;
      this.isEdit = false;
      this.uploadResID = [];
      this.uploadAssID = [];
      this.resFileList = [];
      this.assFileList = [];
      this.form = {
        topic: '',
        reference: '',
        week: '',
        description: '',
        title: '',
        due: '',
      };
    },
    handleResPreview(file) {
      console.log(file);
      this.innerVisible = true;
      this.isRes = true;
      if (file.status === 'success') {
        this.form.fileID = file.id;
        this.form.description = file.description;
      } else {
        this.form.fileID = this.fileToID[file.uid];
        this.form.description = '';
      }
    },
    handleAssPreview(file) {
      console.log(file);
      this.innerVisible = true;
      this.isRes = false;
      console.log(file.due);
      if (file.status === 'success') {
        this.form.fileID = file.id;
        this.form.title = file.title;
        this.form.due = file.due;
      } else {
        this.form.fileID = this.fileToID[file.uid];
        this.form.title = '';
        this.form.due = '';
      }
    },
    removeRes(file, fileList) {
      console.log(file, fileList);
      let rid = 0;
      if (this.isEdit) {
        rid = file.id;
      } else {
        rid = this.fileToID[file.uid];
      }
      this.axios.delete(`/api/v1/resources/${rid}`)
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    removeAss(file, fileList) {
      console.log(file, fileList);
      let aid = 0;
      if (this.isEdit) {
        aid = file.id;
      } else {
        aid = this.fileToID[file.uid];
      }
      this.axios.delete(`/api/v1/assignments/${aid}`)
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    uploadRes(params) {
      const formData = new FormData();
      formData.append('file', params.file);
      formData.append('description', '');
      const url = `/api/v1/courses/${this.$route.params.cid}/resources`;
      this.axios.post(url,
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((res) => {
          console.log(res);
          this.uploadResID.push(res.data.id);
          this.fileToID[params.file.uid] = res.data.id;
        });
    },
    uploadAss(params) {
      const formData = new FormData();
      formData.append('file', params.file);
      formData.append('title', '');
      formData.append('due', '');
      const url = `/api/v1/courses/${this.$route.params.cid}/assignments`;
      this.axios.post(url,
        formData,
        {
          headers: { 'Content-Type': 'multipart/form-data' },
        })
        .then((res) => {
          console.log(res);
          this.uploadAssID.push(res.data.id);
          this.fileToID[params.file.uid] = res.data.id;
        });
    },
    deleteSchedule(id) {
      this.axios.delete(`/api/v1/schedules/${id}`)
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
          this.dialogVisible = false;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    thumbnailFilename(filename) {
      let res = '';
      if (filename.length < 7) {
        res = filename;
      } else {
        res = `${filename.substr(0, 5)}...${filename.match(/.\..*/g)}`;
      }
      return res;
    },
    handleClose(done) {
      this.$confirm('确认关闭？')
        .then((_) => {
          console.log(_);
          this.resFileList.forEach((item) => {
            if (item.status === 'ready') {
              this.removeRes(item, this.resFileList);
            }
          });
          this.assFileList.forEach((item) => {
            if (item.status === 'ready') {
              this.removeAss(item, this.resFileList);
            }
          });
          done();
        })
        .catch((_) => { console.log(_); });
    },
  },
  computed: {
    maxLecsNum() {
      let maxNum = 0;
      this.schedules.forEach((item) => {
        if (item.lectures.length > maxNum) {
          maxNum = item.lectures.length;
        }
      });
      return maxNum;
    },
    schedules() {
      return this.schedulesFilter(this.allInfo.schedules);
    },
  },
};
</script>

<style scoped>
.schedule {
  margin: 50px auto;
  width: 900px;
  height: 100%;
}

.inner-list {
  margin: 10px 30px;
}

.btn-adder:hover {
  color: #409eff;
  background-color: #f9fafc;
}

.click-area {
  cursor: pointer;
}

.light-text {
  font-size: 12px;
}

.btn-adder {
  border: 1px solid #eaeefb;
  height: 44px;
  box-sizing: border-box;
  border-bottom-left-radius: 4px;
  border-bottom-right-radius: 4px;
  text-align: center;
  line-height:30px;
  margin-top: -1px;
  color: #d3dce6;
  cursor: pointer;
  position: relative;
}
#title {
  margin-top: 20px;
}
</style>>
