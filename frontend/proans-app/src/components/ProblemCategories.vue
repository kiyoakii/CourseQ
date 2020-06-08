<template>
  <div>
    <!-- This is ProblemCategories component. -->
    <el-scrollbar>
      <ul class="category-list">
        <li v-for="(item, i) in categories" :key="i"
        style="display: block;">
           <router-link :to="'/proans/1/category/' + item.id + '/problem/0'">
            <el-button :icon="activeCategory === item.id ? 'el-icon-folder-opened':'el-icon-folder'"
            :class="item.type" class="category-item"
            @click="chooseCategory(item.id)">
              {{ item.name }}
            </el-button>
           </router-link>
        </li>
      </ul>
    </el-scrollbar>
  </div>
</template>

<script>
export default {
  name: 'ProblemCategories',
  data() {
    return {
      activeCategory: '0',
      categories: [],
    };
  },
  methods: {
    chooseCategory(id) {
      this.activeCategory = id;
    },
  },
  mounted() {
    this.axios.get('/v1/proans/categories?id=1')
      .then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        this.categories = res.data.data.categories;
      });
  },
};
</script>

<style scoped>

.el-scrollbar {
  margin-left: 20px;
}

a {
  text-decoration: none;
}

.homework {
  color: #409eff;
  background-color: #ecf5ff;
  border-color: #b3d8ff;
}

.exam {
  background-color: yellow;
}

.category-list {
  display: flex;
}

.category-item {
  display: flex;
  height: 100%;
  margin: 0 1em;
}


</style>
