<template>
  <div>
    <el-container>
      <el-header>
        <vue-header></vue-header>
      </el-header>
      <el-main>
        <el-row type="flex" justify="center">
          <el-col :xs="24" :sm="24" :md="22" :lg="22" :xl="22" >
            <el-container>
              <el-aside>
                <search></search>
                <problem-list></problem-list>
              </el-aside>
              <el-main>
                <router-view></router-view>
              </el-main>
            </el-container>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import VueHeader from '@/views/VueHeader.vue';
import ProblemList from '@/components/ProblemList.vue';
import Search from '@/components/Search.vue';

export default {
  name: 'VueContent',
  components: {
    VueHeader,
    ProblemList,
    Search,
  },
};
</script>

<style>

</style>
