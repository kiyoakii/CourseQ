<template>
  <div>
    <!-- This is ProblemCategories component. -->
    <el-scrollbar>
      <ul class="category-list">
        <li v-for="(item, i) in categories" :key="i"
        style="display: block;">
          <el-button :icon="String(activeCategory) === String(item.id) ?
          'el-icon-folder-opened':'el-icon-folder'"
          :class="item.type" class="category-item"
          @click="chooseCategory(item.id)">
            {{ item.name }}
          </el-button>
        </li>
        <li v-if="categories.length === 0">
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
    };
  },
  methods: {
    chooseCategory(id) {
      if (this.activeCategory !== id) {
        this.activeCategory = id;
        this.$router.push({
          path: '/proans/',
          name: 'CategoryView',
          query: {
            tid: id,
          },
        });
      }
    },
  },
  mounted() {
    setTimeout(() => {
      if (this.$route.query.tid !== undefined) {
        this.activeCategory = this.$route.query.tid;
      }
    }, 2000);
  },
  computed: {
    categories() {
      return this.$store.getters.allTags;
    },
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
