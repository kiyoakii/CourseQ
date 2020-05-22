<template>
  <div>
    <ul class="infinite-list" v-infinite-scroll="load" style="overflow:auto">
      <li v-for="(problem, index) in plist" :key=" problem.id " class="infinite-list-item">
        <el-card class="box-card" shadow="hover">
          <div slot="header" class="clearfix">
            <router-link :to="'/proans/1/problem/' + index" class="link">
              <span>{{ problem.title }}</span>
            </router-link>
          </div>
          <div class="text item">
            {{ problem.desc | formatDesc }}
          </div>
        </el-card>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ProblemList',
  data() {
    return {
      count: 0,
      plist: [
        {
          id: 0,
          title: '动态规划',
          desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
                 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
        },
        {
          id: 1,
          title: '贪心算法',
          desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
                 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
        },
        {
          id: 2,
          title: '贪心算法1',
          desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
                 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
        },
        {
          id: 3,
          title: '贪心算法2',
          desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
                 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
        },
        {
          id: 4,
          title: '贪心算法3',
          desc: `动态规划相信大家都知道，但是动态规划到底是什么呢，下面小编给大家介绍一下吧。动态
                 规划就是一种算法，怎么样，大家有什么想法可以在评论区写下来一起分享。`,
        },
      ],
    };
  },
  methods: {
    load() {
      this.count += 2;
    },
  },
  filters: {
    formatDesc(value) {
      return value.length <= 50 ? value : `${value.slice(0, 50)}...`;
    },
  },
};
</script>

<style scoped>
.box-card {
  font-weight: 600;
  margin-bottom: 15px;
  cursor: pointer;
}

.box-card:hover {
  background: rgba(250, 250, 250, .8);
}

.text {
  font-size: 12px;
}

.link {
  text-decoration: none;
  color: #303133;
  display: block;
}
</style>
