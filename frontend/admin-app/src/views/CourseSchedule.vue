<template>
  <div>
    <el-card shadow="always">
      <div slot="header">
        <h1>Schedule</h1>
      </div>
      <el-card>
        <el-table :data="schedule" :header-cell-style="{'text-align':'center'}"
                      highlight-current-row size="medium">
          <el-table-column prop="week" label="Week" width="100" align="center"
                      style="font-weight:bold"></el-table-column>
          <el-table-column label="topic"
                      width="260" align="left" :show-overflow-tooltip="true">
            <template slot-scope="scope">
              <div>
                <ul>
                  <li v-for="(value, index) in scope.row.courseOne" :key="index">
                    {{`${index}:${value}`}}
                  </li>
                </ul>
              </div>
            </template>
          </el-table-column>
          <el-table-column width="260" align="left"
            :show-overflow-tooltip="true">
            <template slot-scope="scope">
              <div>
                <ul>
                  <li v-for="(value, index) in scope.row.courseTwo" :key="index">
                    {{`${index}:${value}`}}
                  </li>
                </ul>
              </div>
            </template>
          </el-table-column>
        </el-table>
      </el-card>
    </el-card>
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
            week: 'Week1',
            courseOne: null,
            courseTwo: {
              lecture: 'Lec1',
              describe: 'Introduction',
              reference: 'xxx',
            },
          },
          {
            week: 'Week2',
            courseOne: {
              lecture: 'Lec2',
              describe: '如何选购扫地机器人',
              reference: 'xxx',
            },
            courseTwo: {
              lecture: 'Lec3',
              describe: '一阶逻辑',
              reference: 'xxx',
            },
          },
        ];
      },
    },
  },
};
</script>

<style>

</style>
