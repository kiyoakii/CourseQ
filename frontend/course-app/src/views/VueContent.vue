<template>
  <div>
    <router-view :allinfo="allinfo"></router-view>
  </div>
</template>

<script>
export default {
  name: 'VueContent',
  data() {
    return {
      allinfo: {},
    };
  },
  mounted() {
    // this.axios.get('/v1/course/allinfo?id=1')
    //   .then((res) => {
    //     console.log(res);
    //     if (res.status !== 200) {
    //       console.log(JSON.stringify(res.data));
    //       return;
    //     }
    //     this.allinfo = res.data.data;
    //   });
    this.axios.get('/api/v1/courses')
      .then((res) => {
        console.log(111, res);
      });
  },
};
</script>

<style>

</style>
