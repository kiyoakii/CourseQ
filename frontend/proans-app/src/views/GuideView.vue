<template>
  <div>
    <el-card>
       <div class="block">
        <el-carousel height="300px">
          <el-carousel-item v-for="item in text" :key="item">
            <h1 class="small">{{ item }}</h1>
          </el-carousel-item>
        </el-carousel>
      </div>
    </el-card>
  </div>
</template>

<script>
export default {
  name: 'GuideView',
  computed: {
    text() {
      if (this.$store.getters.allProblems.length === 0) {
        return ['暂时没有问题噢，点击左侧添加问题'];
      }
      return [
        '顶部可选择问题所属分类',
        '选择分类后可在左侧点击对应问题显示',
        '左侧顶部有查询框，可用来查询问题',
        '新建问题请点击左侧加号',
      ];
    },
  },
  beforeMount() {
    this.$store.commit({
      type: 'setCid',
      id: Number(this.$route.params.cid),
    });
    this.$store.dispatch('initProblems');
  },
};
</script>

<style scoped>
.el-carousel__item h1 {
  color: #475669;
  font-size: 20px;
  opacity: 0.75;
  line-height: 150px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
    background-color: #effaff;
}

.el-carousel__item:nth-child(2n+1) {
    background-color: #ecf5ff;
}

.el-carousel__item {
  display: flex;
  justify-content: center;
  align-items: center;
}

</style>
