<template>
  <div>
    <!-- This is TeacherInfo view. -->
    <el-card class="box-card">
      <div id="teacher-info">
        <el-row>
          <el-col :span="8">
            <div class="grid-content bg-purple info-label">
              <h3>Teacher:</h3>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple-light">
              <p>{{teacherInfo.teacher}}</p>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple-light">
              <p>{{teacherInfo.teacherEmail}}</p>
            </div>
          </el-col>
          <el-col :span="4">
            <div class="grid-content bg-purple-light">
              <p>{{teacherInfo.teacherPhone}}</p>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="8">
            <div class="grid-content bg-purple info-label">
              <h3>TAs:</h3>
            </div>
          </el-col>
          <el-col :span="4">
            <div v-for="(item, i) in teacherInfo.assistant" :key="i">
              <el-row>
                <div class="grid-content bg-purple-light">
                  <p>{{item}}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="4">
            <div v-for="(item, i) in teacherInfo.assistantEmail" :key="i">
              <el-row>
                <div class="grid-content bg-purple-light">
                  <p>{{item}}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="4">
            <div v-for="(item, i) in teacherInfo.assistantPhone" :key="i">
              <el-row>
                <div class="grid-content bg-purple-light">
                  <p>{{item}}</p>
                </div>
              </el-row>
            </div>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'TeacherInfo',
  props: {
    teacherInfo: {
      type: Object,
      default() {
        return {
          teacher: 'TeacherName',
          teacherEmail: 'teacher@mail.com',
          teacherPhone: '12312341234',
          assistant: ['Assistant1', 'Assistant2'],
          assistantEmail: ['ta1@mail.com', 'ta2@mail.com'],
          assistantPhone: ['12312341234', '12312341234'],
        };
      },
    },
  },
};
</script>

<style scoped>
#teacher-info {
  display: flex;
  flex-direction: column;
}
.info-label {
  display: flex;
  /* align-items: center; */
  justify-content:center;
}

</style>
