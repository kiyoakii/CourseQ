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
            if (String(t.id) === String(tid)) {
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
      return (pid) => state.problems.find((p) => String(p.id) === String(pid));
    },
    tag(state) {
      return (tid) => state.tags.find((t) => String(t.id) === String(tid));
    },
  },
  mutations: {
    initProblems(state, problems) {
      state.problems.splice(0, state.problems.length);
      state.problems.push(...problems);
      const tags = [];
      state.problems.forEach((p) => {
        p.tags.forEach((t) => {
          if (tags.find((ta) => ta.name === t.name) === undefined) {
            tags.push(t);
          }
        });
      });
      state.tags.splice(0, state.tags.length);
      state.tags.push(...tags);
    },
    updateProblem(state, problem) {
      const i = state.problems.findIndex((p) => String(p.id) === String(problem.id));
      state.problems[i] = problem;
      const tags = [];
      state.problems.forEach((p) => {
        p.tags.forEach((t) => {
          if (tags.find((ta) => ta.name === t.name) === undefined) {
            tags.push(t);
          }
        });
      });
      state.tags.splice(0, state.tags.length);
      state.tags.push(...tags);
    },
    deleteProblem(state, problem) {
      const i = state.problems.findIndex((p) => String(p.id) === String(problem.id));
      state.problems.splice(i, 1);
      const tags = [];
      state.problems.forEach((p) => {
        p.tags.forEach((t) => {
          if (tags.find((ta) => ta.name === t.name) === undefined) {
            tags.push(t);
          }
        });
      });
      state.tags.splice(0, state.tags.length);
      state.tags.push(...tags);
    },
  },
  actions: {
    initProblems(context, cid) {
      axios.get(`/api/v1/courses/${cid}/questions`)
        .then((res) => {
          if (res.status === 200) {
            context.commit('initProblems', res.data);
          }
        });
    },
    updateProblem(context, problem) {
      axios.get(`/api/v1/questions/${problem.id}`)
        .then((res) => {
          console.log(res);
          if (res.status === 200) {
            context.commit('updateProblem', res.data);
          }
        });
    },
  },
  modules: {
  },
});
