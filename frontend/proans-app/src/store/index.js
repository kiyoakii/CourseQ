import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    problems: [],
    tags: [],
    count: 0,
  },
  getters: {
    allProblems(state) {
      return state.problems;
    },
    allTags(state) {
      return state.tags;
    },
    problemsByTag(state) {
      return (tid) => {
        const problems = [];
        state.problems.forEach((p) => {
          p.tags.forEach((t) => {
            if (t.id === tid) {
              problems.push(p);
            }
          });
        });
        return problems;
      };
    },
    problemsBySearch(state, getters) {
      return (searchInfo) => {
        const problems = [];
        let temp = [];
        if (searchInfo.select !== '') {
          temp = getters.problemsByTag(searchInfo.select);
          temp.forEach((p) => {
            if (p.title.search(searchInfo.searchText) !== -1) {
              problems.push(p);
            }
          });
        } else {
          state.problems.forEach((p) => {
            if (p.title.search(searchInfo.searchText) !== -1) {
              problems.push(p);
            }
          });
        }
        return problems;
      };
    },
    problem(state) {
      return (pid) => state.problems.find((p) => String(p.id) === pid);
    },

  },
  mutations: {
    initProblems(state, problems) {
      state.problems.splice(0, state.problems.length);
      state.problems.push(...problems);
      const tags = [];
      state.problems.forEach((p) => {
        p.tags.forEach((t) => {
          if (!tags.includes(t)) {
            tags.push(t);
          }
        });
      });
      state.tags.splice(0, state.tags.length);
      state.tags.push(...tags);
    },
  },
  actions: {
    initProblems(context) {
      axios.get('/api/v1/courses/3/questions')
        .then((res) => {
          if (res.status === 200) {
            context.commit('initProblems', res.data);
          }
        });
    },
  },
  modules: {
  },
});
