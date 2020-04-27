<template>
  <div>
    <!-- This is CourseSchedule view. -->
    <el-card shadow="always">
      <div slot="header">
        <h1>Schedule</h1>
      </div>
      <el-card>
        <el-table :data="schedule" highlight-current-row size="medium">
          <el-table-column prop="week" label="Week" width="100" align="center"
            style="font-weight:bold"></el-table-column>
          <el-table-column label="Course 1st" width="260" align="left"
            :show-overflow-tooltip="true">
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
          <el-table-column label="Course 2nd" width="260" align="left"
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
          <el-table-column prop="assignments" label="Assignments" align="left"></el-table-column>
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
            assignments: 'Homework 1',
          },
        ];
      },
    },
  },
};
</script>

<style scoped>

</style>
