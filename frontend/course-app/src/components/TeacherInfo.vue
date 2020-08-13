<template>
  <div>
    <!-- This is TeacherInfo view. -->
    <el-card class="box-card">
      <div id="teacher-info">
        <el-row class="teacher-list">
          <el-col :span="6">
            <div class="grid-content bg-purple info-label">
              <h3>Teacher:</h3>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(teacher, i) in allinfo.teachers" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ teacher.name }}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(teacher, i) in allinfo.teachers" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ teacher.email }}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(teacher, i) in allinfo.teachers" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ teacher.phone }}</p>
                </div>
              </el-row>
            </div>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="6">
            <div class="grid-content bg-purple info-label">
              <h3>TAs:</h3>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(item, i) in allinfo.assistants" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ item.name }}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(assistant, i) in allinfo.assistants" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ assistant.email }}</p>
                </div>
              </el-row>
            </div>
          </el-col>
          <el-col :span="6">
            <div v-for="(assistant, i) in allinfo.assistants" :key="i">
              <el-row style="height:18px;">
                <div class="grid-content bg-purple-light">
                  <p>{{ assistant.phone }}</p>
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
    allinfo: {},
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
.teacher-list {
  margin-bottom: 10px;
}
</style>
