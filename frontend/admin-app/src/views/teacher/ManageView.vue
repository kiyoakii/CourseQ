<template>
  <div>
    <el-container>
      <side-bar></side-bar>
      <router-view :allInfo="allInfo"></router-view>
    </el-container>
  </div>
</template>

<script>
import SideBar from '@/components/SideBar.vue';

export default {
  name: 'ManageView',
  components: {
    SideBar,
  },
  data() {
    return {
      allInfo: {},
    };
  },
  mounted() {
    this.axios.get('/v1/admin/teacher/course/allinfo?course=1&semester=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.allInfo = res.data.allInfo;
      });
  },
};
</script>

<style>

</style>
