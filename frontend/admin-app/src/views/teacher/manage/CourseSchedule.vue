<template>
  <div>
    <h2 id="title">日程安排</h2>
    <div class="schedule">
      <el-table :data="allInfo.schedules" :header-cell-style="{'text-align':'center'}"
        highlight-current-row size="medium">
        <el-table-column prop="week_id" label="教学周" width="100" align="center"
          style="font-weight:bold"></el-table-column>
        <el-table-column label="课程"
          align="left" :show-overflow-tooltip="true">
          <el-table-column v-for="i in maxLecsNum" :key="i" :label="`lec${i}`"
          align="left" :show-overflow-tooltip="true">
            <el-table-column label="主题">
              <template slot-scope="scope">
                {{ scope.row.lectures.length >= i
                ? scope.row.lectures[i - 1].title : '' }}
              </template>
            </el-table-column>
            <el-table-column label="教学资源">
              <template slot-scope="scope">
                <el-row v-for="(res, index) in
                scope.row.lectures.length >= i
                ? scope.row.lectures[i - 1].resources : []" :key="index">
                    <el-link type="primary" :href="res.url">{{ res.title }}</el-link>
                </el-row>
              </template>
            </el-table-column>
            <el-table-column label="作业">
              <template slot-scope="scope">
                <el-row v-for="(ass, index) in
                scope.row.lectures.length >= i
                ? scope.row.lectures[i - 1].assignments : []" :key="index">
                    <el-link type="primary" :href="ass.url">{{ ass.title }}</el-link>
                </el-row>
              </template>
            </el-table-column>
          </el-table-column>
          <el-table-column label="添加">
            <template slot-scope="scope">
              <div class="btn-adder"
                @click="addLecs(scope.row)">
                <i class="el-icon-plus"></i>
              </div>
            </template>
          </el-table-column>
        </el-table-column>
      </el-table>
      <div class="btn-adder"
        @click="addWeeks">
        <i class="el-icon-plus"></i>
      </div>
      <el-dialog
        :title="'添加'"
        :visible.sync="dialogVisible"
        width="720px">
        <el-form :model="form">
          <el-form-item label="主题" >
            <el-input v-model="form.title" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="教学资源" >
            <el-upload
              class="upload-demo"
              drag
              action="https://jsonplaceholder.typicode.com/posts/"
              :file-list="fileList"
              :on-preview="handlePreview"
              multiple>
              <i class="el-icon-upload"></i>
              <div class="el-upload__text">将文件拖到此处，或<em>点击上传</em></div>
            </el-upload>
          </el-form-item>
          <el-form-item label="作业" >
            <el-input type="file" v-model="form.content" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <span slot="footer" class="dialog-footer">
          <el-button @click="dialogVisible = false">取 消</el-button>
          <el-button type="primary" @click="submit">确 定</el-button>
        </span>
      </el-dialog>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CourseSchedule',
  props: {
    schedule: {
      type: Array,
      default() {
        return [
          {
            id: 1,
            week_id: 1,
            lectures: [
              {
                title: 'title1',
                resources: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                  {
                    url: 'String1',
                    title: 'String1',
                  },
                ],
                assignments: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
              },
              {
                title: 'title2',
                resources: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
                assignments: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
              },
              {
                title: 'title4',
                resources: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
                assignments: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
              },
            ],
          },
          {
            id: 2,
            week_id: 2,
            lectures: [
              {
                title: 'title3',
                resources: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
                assignments: [
                  {
                    url: 'String',
                    title: 'String',
                  },
                ],
              },
            ],
          },
        ];
      },
    },
    allInfo: {},
  },
  data() {
    return {
      dialogVisible: false,
      form: {
        id: '',
        res: '',
        ass: '',
      },
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      fileList: [],
    };
  },
  methods: {
    submit() {
      console.log('submit');
    },
    handleEdit(lec) {
      console.log(lec);
    },
    addWeeks() {
      let weekId = 1;
      if (this.allInfo.schedules.length !== 0) {
        weekId = this.allInfo.schedules[this.allInfo.schedules.length - 1].weekId + 1;
      }
      console.log(weekId);
      this.axios.post(`/api/v1/courses/${this.$route.params.cid}/schedules`,
        {
          week: weekId,
          topic: 'sdfsdf',
          reference: 'sdfawe',
        })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
    },
    addLecs(row) {
      console.log(row);
      this.dialogVisible = true;
    },
    handlePreview(file) {
      console.log(file);
    },
  },
  computed: {
    maxLecsNum() {
      let maxNum = 0;
      this.schedule.forEach((item) => {
        if (item.lectures.length > maxNum) {
          maxNum = item.lectures.length;
        }
      });
      return maxNum > 4 ? 4 : maxNum;
    },
  },
};
</script>

<style scoped>
.schedule {
  margin: 50px auto;
}

.inner-list {
  margin: 10px 30px;
}

.btn-adder:hover {
  color: #409eff;
  background-color: #f9fafc;
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
