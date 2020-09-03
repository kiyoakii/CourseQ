<template>
  <div class="el-col">
    <el-scrollbar style="height: 100%;">
      <el-row class="category-list" type="flex" align="center">
        <el-col v-for="(item, i) in categories" :key="i"
        style="display: block;">
          <el-button :icon="String(activeCategory) === String(item.id) ?
          'el-icon-folder-opened':'el-icon-folder'"
          :class="String(activeCategory) === String(item.id) ?
          'folder-opened' : 'folder-closed'" class="category-item"
          @click="chooseCategory(item.id)">
            {{ item.name }}
          </el-button>
        </el-col>
        <el-col v-if="categories.length === 0">
        </el-col>
      </el-row>
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
      this.$emit('click');
      if (this.activeCategory !== id) {
        this.activeCategory = id;
        this.$router.push({
          name: 'CategoryView',
          params: {
            cid: this.$route.params.cid,
            tid: id,
          },
        }).catch(() => {});
      }
    },
  },
  watch: {
    $route() {
      if (this.$route.params.tid !== undefined) {
        this.activeCategory = this.$route.params.tid;
      }
    },
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

.category-list {
  display: flex;
  align-items: center;
}

.category-item {
  display: flex;
  height: 100%;
  margin: 0 1em;
}

.folder-opened  {
  background-color: #ecf5ff;
  color: #409eff;
}

.el-col {
  height: 100%;
}

</style>

<style>

.el-scrollbar .el-scrollbar__wrap {
  display: flex;
  align-items: center;
  overflow-x: hidden;
}
</style>
