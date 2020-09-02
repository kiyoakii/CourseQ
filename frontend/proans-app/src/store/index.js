import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import VuexPersistence from 'vuex-persist';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    problems: [],
    tags: [],
    count: 0,
    qid: 0,
    cid: 0,
    gid: '',
    clickLike: false, // 点击我的点赞
    proansToken: '',
    auth: '',
    commentList: [],
  },
  getters: {
    commentList(state) {
      return state.commentList;
    },
    allProblems(state) {
      return state.problems;
    },
    allTags(state) {
      return state.tags;
    },
    problemsByLike(state) {
      return state.problems.filter((problem) => problem.liked === true);
    },
    problemsByTag(state) {
      return (tid) => {
        if (!tid) {
          return state.problems;
        }
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
    problemsBySearch(state) {
      return (searchInfo) => {
        const problems = [];
        state.problems.forEach((p) => {
          if (p.title.search(searchInfo) !== -1
          || p.content.search(searchInfo) !== -1) {
            problems.push(p);
          }
        });
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
    setGid(state, gid) {
      state.gid = gid;
    },
    setClickLike(state, { like }) {
      state.clickLike = like;
    },
    setAuth(state, scope) {
      if (scope === 'StudentScope') {
        state.auth = '学生';
      } else if (scope === 'TeacherScope') {
        state.auth = '教师';
      } else if (scope === 'AdminScope') {
        state.auth = '管理员';
      }
    },
    changeStudentAnswer(state, { content }) {
      const index = state.problems.findIndex((problem) => problem.id === state.qid);
      console.log('index:', index);
      console.log('change stu_ans: ', {
        ...state.problems[index],
        student_answer: {
          ...state.problems[index].student_answer,
          content,
        },
      });
      if (index >= 0 && index < state.problems.length) {
        state.problems.splice(index, 1, {
          ...state.problems[index],
          student_answer: {
            ...state.problems[index].student_answer,
            content,
          },
        });
      }
    },
    setCommentList(state, { list }) {
      state.commentList.splice(0, state.commentList.length);
      state.commentList.push(...list);
    },
    setQid(state, { id }) {
      state.qid = id;
    },
    setCid(state, { id }) {
      state.cid = id;
    },
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
      state.problems.splice(i, 1, problem);
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
    setProansToken(state, token) {
      state.proansToken = token;
    },
  },
  actions: {
    initProblems(context) {
      console.log('initProblem', context.state.proansToken);
      axios.get(`/api/v1/courses/${context.state.cid}/questions`, {
        headers: {
          Authorization: `Bearer ${context.state.proansToken}`,
        },
      }).then((res) => {
        if (res.status === 200) {
          context.commit('initProblems', res.data);
        }
      });
    },
    updateProblem(context, problem) {
      console.log(111, problem);
      axios.get(`/api/v1/questions/${problem.id || context.state.qid}`, {
        headers: {
          Authorization: `Bearer ${context.state.proansToken}`,
        },
      }).then((res) => {
        console.log(333, res);
        if (res.status === 200) {
          context.commit('updateProblem', res.data);
        }
      });
    },
    setCommentList(context) {
      axios.get(`/api/v1/questions/${context.state.qid}/discussions`, {
        headers: {
          Authorization: `Bearer ${context.state.proansToken}`,
        },
      }).then((res) => {
        console.log(res);
        if (res.status !== 200) {
          console.log(JSON.stringify(res.data));
          return;
        }
        context.commit({
          type: 'setCommentList',
          list: res.data,
        });
      });
    },
  },
  modules: {
  },
  plugins: [
    new VuexPersistence().plugin,
  ],
});
