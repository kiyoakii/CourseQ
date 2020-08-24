<template>
  <div>
    <h2 id="title">日程安排</h2>
    <div class="schedule">
      <el-table :data="schedules.schedules"
        border
        :header-cell-style="{'text-align':'center'}"
        :span-method="arraySpanMethod"
        highlight-current-row>
        <el-table-column prop="week" label="教学周"
          width="70"
          align="center"
          fixed
          style="font-weight:bold"></el-table-column>
        <el-table-column label="上课时间"
          prop="datetime"
          align="center"
          width="100">
        </el-table-column>
        <el-table-column label="主题"
          width="120"
          prop="topic"
          align="center">
            <template slot-scope="scope">
              <el-row>
                <span>
                {{ scope.row.topic }}
                </span>
              </el-row>
              <el-row>
                <span class="light-text">
                  {{ `参考章节：${scope.row.reference}` }}</span>
              </el-row>
            </template>
          </el-table-column>
          <el-table-column label="教学资源"
          min-width="120"
          align="center">
            <template slot-scope="scope">
              <el-row v-for="(res, index) in scope.row.resources" :key="index">
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
              <el-row v-for="(ass, index) in scope.row.assignments" :key="index"
              :gutter="20">
                  <el-row>
                    <span>{{ ass.title === '无' ? '' : ass.title }}</span>
                  </el-row>
                  <el-row>
                    <el-link type="primary" :href="ass.url">
                      {{ thumbnailFilename(ass.filename) }}</el-link>
                  </el-row>
                  <el-row class="light-text">
                    <span>ddl:{{ ass.ddl }}</span>
                  </el-row>
              </el-row>
            </template>
          </el-table-column>
          <el-table-column label="补充" prop="additional_info">
          </el-table-column>
          <el-table-column label="操作"
          align="center"
            width="200">
            <template slot-scope="scope">
              <el-button size="small"
                type="primary"
                icon="el-icon-edit"
              @click="handleEdit(scope.row)">编辑</el-button>
              <el-button type="danger" size="small"
                icon="el-icon-delete"
              @click="deleteSchedule(scope.row)">删除</el-button>
            </template>
          </el-table-column>
      </el-table>
      <div class="btn-adder"
        @click="createSchedule">
        <i class="el-icon-plus"></i>
        <span>新增日程</span>
      </div>
      <el-dialog
        :title="isEdit ? '编辑' : '添加'"
        :visible.sync="dialogVisible"
        :before-close="handleClose"
        width="720px">
        <el-form :model="form" label-width="80px"
          :rules="rules"
          ref="lecForm">
          <el-form-item label="主题" prop="topic">
            <el-input v-model="form.topic"
              maxlength="20"
              show-word-limit></el-input>
          </el-form-item>
          <el-form-item label="参考章节" >
            <el-input v-model="form.reference" autocomplete="off"
              maxlength="20"
              show-word-limit></el-input>
          </el-form-item>
          <el-form-item label="教学周" prop="week">
            <el-select v-model="form.week">
              <el-option v-for="i in weekNum"
              :key="String(i)"
              :value="i"
              :label="String(i)">
              </el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="上课时间" required>
            <el-col :span="11">
              <el-form-item prop="timeW">
                <el-select v-model="form.timeW"
                placeholder="请选择周次">
                  <el-option
                    v-for="item in optionsTimeW"
                    :key="item"
                    :label="item"
                    :value="item">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
            <el-col :span="11">
              <el-form-item prop="timeL">
                <el-select v-model="form.timeL"
                placeholder="请选择节次">
                  <el-option
                    v-for="i in lecNum"
                    :key="i"
                    :label="`第${i}节`"
                    :value="`第${i}节`">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-col>
          </el-form-item>
          <el-form-item label="教学资源" >
            <el-upload
              drag
              :headers="headers"
              action="eadf"
              :file-list="resFileList"
              :on-preview="handleResPreview"
              :on-remove="removeRes"
              :http-request="uploadRes">
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或<em>点击上传</em>
              </div>
              <div slot="tip" class="el-upload__tip">点击文件添加资源描述</div>
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
              :http-request="uploadAss">
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">
                将文件拖到此处，或<em>点击上传</em>
              </div>
              <div slot="tip" class="el-upload__tip">点击文件添加作业描述</div>
            </el-upload>
          </el-form-item>
          <el-form-item label="补充" prop="additionalInfo">
            <el-input type="textarea"
              v-model="form.additionalInfo"
              maxlength="50"
              show-word-limit></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="handleClose(() => { dialogVisible = false })">取 消</el-button>
          <el-button type="primary" @click="submit">确 定</el-button>
        </span>
        <el-dialog
        :visible.sync="innerVisible"
        append-to-body>
          <el-form>
            <el-form-item :label="isRes ? '资源描述' : '作业描述'">
              <el-input v-if="isRes" v-model="form.description"
              placeholder="请输入资源描述"
              maxlength="20"
              show-word-limit></el-input>
              <el-input v-else v-model="form.title"
              placeholder="请输入作业描述"
              maxlength="20"
              show-word-limit></el-input>
            </el-form-item>
            <el-form-item v-if="!isRes"
            label="选择截止日期">
              <el-date-picker
                v-model="form.ddl"
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
        ddl: '',
        timeW: '',
        timeL: '',
        additionalInfo: '',
      },
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      resFileList: [],
      assFileList: [],
      fileToID: [],
      uploadResID: [],
      uploadAssID: [],
      optionsTimeW: ['周一', '周二', '周三', '周四', '周五', '周六', '周日'],
      lecNum: 14,
      weekNum: 18,
      rules: {
        topic: [
          { required: true, message: '请输入课程主题', trigger: 'blur' },
        ],
        week: [
          { required: true, message: '请输入教学周', trigger: 'blur' },
          { type: 'number', message: '请输入正确的教学周' },
        ],
        timeW: [
          { required: true, message: '请输入上课周次', trigger: 'blur' },
        ],
        timeL: [
          { required: true, message: '请输入上课节次', trigger: 'blur' },
        ],
      },
    };
  },
  methods: {
    arraySpanMethod(params) {
      if (params.columnIndex === 0) {
        const weekInfo = this.schedules.weekInfo.find((item) => item.week === params.row.week);
        if (params.row.id === weekInfo.lectures[0].id) {
          return {
            rowspan: weekInfo.lectures.length,
            colspan: 1,
          };
        }
        return {
          rowspan: 0,
          colspan: 0,
        };
      }
      return {
        rowspan: 1,
        colspan: 1,
      };
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
        formData.append('ddl', this.form.ddl.toLocaleString('zh-CN'));
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
      this.$refs.lecForm.validate((valid) => {
        if (valid) {
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
              additional_info: this.form.additionalInfo,
              datetime: `${this.form.timeW}${this.form.timeL}`,
              resource_ids: this.uploadResID,
              assignment_ids: this.uploadAssID,
            },
          })
            .then((res) => {
              console.log(res);
              this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
            })
            .catch((err) => {
              console.log(err.response);
            });
          this.dialogVisible = false;
        } else {
          console.log('error submit!!');
          return false;
        }
        return true;
      });
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
        title: '',
        ddl: '',
        additionalInfo: lec.additional_info,
        timeW: lec.datetime.substr(0, 2),
        timeL: lec.datetime.substr(2),
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
          ddl: new Date(item.ddl.replace('上午', '').replace('下午', '').replace('中午', '')),
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
        ddl: '',
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
      console.log(file.ddl);
      if (file.status === 'success') {
        this.form.fileID = file.id;
        this.form.title = file.title;
        this.form.ddl = file.ddl;
      } else {
        this.form.fileID = this.fileToID[file.uid];
        this.form.title = '';
        this.form.ddl = '';
      }
    },
    removeRes(file, fileList) {
      console.log(file, fileList);
      let rid = 0;
      if (file.status === 'success') {
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
      if (file.status === 'success') {
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
      formData.append('title', '无');
      formData.append('ddl', '暂无');
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
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    deleteSchedule(row) {
      this.$confirm('确认删除？')
        .then(() => {
          row.resources.forEach((item) => {
            this.axios.delete(`/api/v1/resources/${item.id}`)
              .then((res) => {
                console.log(res);
              })
              .catch((err) => {
                console.log(err.response);
              });
          });
          row.assignments.forEach((item) => {
            this.axios.delete(`/api/v1/assignments/${item.id}`)
              .then((res) => {
                console.log(res);
              })
              .catch((err) => {
                console.log(err.response);
              });
          });
          this.axios.delete(`/api/v1/schedules/${row.id}`)
            .then((res) => {
              console.log(res);
              this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
              this.dialogVisible = false;
            })
            .catch((err) => {
              console.log(err.response);
            });
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
