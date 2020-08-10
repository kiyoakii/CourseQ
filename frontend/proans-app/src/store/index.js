import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    problems: [],
    count: 0,
  },
  getters: {
    allProblems(state) {
      return state.problems;
    },
  },
  mutations: {
    initProblems(state, problems) {
      state.problems.splice(0, state.problems.length);
      state.problems.push(...problems);
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
