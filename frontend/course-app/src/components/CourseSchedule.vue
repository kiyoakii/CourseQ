<template>
  <el-card class="box-card">
    <div class="schedule">
      <el-table :data="schedules.schedules"
        border
        :header-cell-style="{'text-align':'center'}"
        :span-method="arraySpanMethod">
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
                    <a type="primary" :href="res.url" :download="res.filename">
                      {{ thumbnailFilename(res.filename) }}
                    </a>
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
                    <a type="primary" :href="ass.url" :download="ass.filename">
                      {{ thumbnailFilename(ass.filename) }}
                    </a>
                  </el-row>
                  <el-row class="light-text">
                    <span>ddl:{{ ass.ddl }}</span>
                  </el-row>
              </el-row>
            </template>
          </el-table-column>
          <el-table-column label="补充" prop="additional_info">
          </el-table-column>
      </el-table>
    </div>
  </el-card>
</template>

<script>
import { schedulesFilter } from '@/helpers/filters';

export default {
  name: 'CourseSchedule',
  props: {
    allinfo: {},
  },
  data() {
    return {
      schedulesFilter,
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
    thumbnailFilename(filename) {
      let res = '';
      if (filename.length < 7) {
        res = filename;
      } else {
        res = `${filename.substr(0, 5)}...${filename.match(/.\..*/g)}`;
      }
      return res;
    },
  },
  computed: {
    schedules() {
      return this.schedulesFilter(this.allinfo.schedules || []);
    },
  },
};
</script>

<style scoped>
.schedule {
  margin: 0;
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

</style>

<style>
.hover-row>td {
  background-color: #FFF !important;
}
</style>
