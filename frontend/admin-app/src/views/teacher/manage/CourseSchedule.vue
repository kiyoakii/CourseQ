<template>
  <div>
    <h2>日程安排</h2>
    <div class="schedule">
      <el-table :data="allInfo.schedules" :header-cell-style="{'text-align':'center'}"
        highlight-current-row size="medium">
        <el-table-column prop="week_id" label="教学周" width="100" align="center"
          style="font-weight:bold"></el-table-column>
        <el-table-column label="课程"
          align="left" :show-overflow-tooltip="true">
          <el-table-column label="lec1"
          align="left" :show-overflow-tooltip="true">
            <el-table-column label="主题">
              <template slot-scope="scope">
                {{ scope.row.lectures[0].title }}
              </template>
            </el-table-column>
            <el-table-column label="教学资源">
              <template slot-scope="scope">
                <el-row v-for="(res, index) in scope.row.lectures[0].resources" :key="index">
                    <el-link type="primary" :href="res.url">{{ res.title }}</el-link>
                </el-row>
              </template>
            </el-table-column>
            <el-table-column label="作业">
              <template slot-scope="scope">
                <el-row v-for="(ass, index) in scope.row.lectures[0].assignments" :key="index">
                    <el-link type="primary" :href="ass.url">{{ ass.title }}</el-link>
                </el-row>
              </template>
            </el-table-column>
          </el-table-column>
          <el-table-column label="lec2"
          align="left" :show-overflow-tooltip="true">
            <el-table-column label="主题">
            </el-table-column>
            <el-table-column label="教学资源">
            </el-table-column>
            <el-table-column label="作业">
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
        width="1000px">
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
      this.axios.post(`/api/v1/courses/${this.$route.params.cid}/schedules`,
        { week_id: weekId })
        .then((res) => {
          console.log(res);
          this.$store.dispatch('initCourses', { tid: this.$route.params.tid });
        });
    },
    addLecs(row) {
      console.log(row);
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
</style>>
