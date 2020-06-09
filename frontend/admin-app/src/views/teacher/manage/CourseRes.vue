<template>
  <div class="fix-all">
    <el-row v-for="anno in recourses" :key="anno.id">
      <el-card class="card-box">
        <div slot="header" class="clearfix card-header">
          <h2>{{ anno.title }}</h2>
        </div>
        <div>
          {{ anno.content }}
        </div>
        <div class="right-align">
          <el-button type="primary"
          icon="el-icon-edit" size="small">编辑
          </el-button>
          <el-button type="primary"
          icon="el-icon-edit" size="small">删除
          </el-button>
        </div>
      </el-card>
    </el-row>
    <el-row class="upload">
      <el-card class="card-box">
        <div slot="header">
          <h3>上传资源</h3>
        </div>
        <div class="edge">
          资源名称：
          <el-input style="width: 40%" placeholder="资源名称"></el-input>
        </div>
        <div class="edge">
          添加资源：
          <el-input style="width: 40%" placeholder="路径"></el-input>
          <el-button type="primary" class="edge">选择文件</el-button>
        </div>
        <div class="right-align edge">
          <el-button type="primary">上传</el-button>
        </div>
      </el-card>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'CourseAnnounce',
  data() {
    return {
      recourses: [
        {
          title: 'Introduction',
          content: 'Chap1.ppt',
        },
        {
          title: 'Sql',
          content: 'Chap2.ppt',
        },
        {
          title: '数值积分',
          content: 'Chap6.ppt',
        },
      ],
    };
  },
  props: {
    allInfo: {
      type: Object,
      default() {
        return {
          recourses: [
            {
              title: 'Introduction',
              content: 'Chap1.ppt',
            },
            {
              title: 'Lagrange插值',
              content: 'Chap2.ppt',
            },
            {
              title: '数值积分',
              content: 'Chap6.ppt',
            },
          ],
        };
      },
    },
  },
};
</script>

<style>
.fix-all {
  width: 100%;
}
.right-align {
  text-align:right;
}
.upload {
  margin-top: 100px;
}
.edge {
  margin: 10px;
}
</style>
