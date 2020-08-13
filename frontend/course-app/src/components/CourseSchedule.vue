<template>
  <div>
    <!-- This is CourseSchedule view. -->
    <el-card shadow="always" class="box-card">
      <el-table :data="schedule" header-row-class-name="tableHead" highlight-current-row>
        <el-table-column prop="week" label="Week" width="100" align="center"
          style="font-weight:bold"></el-table-column>
        <!-- <el-table-column label="Date" width="260" align="center"
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
        </el-table-column> -->
        <el-table-column prop="date" label="Date" width="100" align="center"
          style="font-weight:bold"></el-table-column>
        <el-table-column prop="lecture" label="Lecture" width="100" align="center"
          style="font-weight:bold"></el-table-column>
        <el-table-column prop="homework" label="Homework" align="center"></el-table-column>
        <el-table-column prop="resource" label="Resource" width="100" align="center"
          style="font-weight:bold"></el-table-column>
      </el-table>
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
            date: '2020-2-17',
            lecture: '',
            homework: 'Homework 1',
            resource: '',
          },
          {
            week: 'Week1',
            date: '2020-2-19',
            lecture: '',
            homework: 'Homework 2',
            resource: '',
          },
        ];
      },
    },
  },
};
</script>

<style scoped>
.tableHead {
  font-size: 40px;
}
</style>
