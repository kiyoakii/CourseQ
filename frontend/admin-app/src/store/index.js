import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';
import axios from 'axios';
import { memberFilter } from '../helpers/filters';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    allCourses: [],
    allTeachers: [],
    allStudents: [],
  },
  getters: {
    adminAllCourses(state) {
      const res = [];
      state.allCourses.forEach((item) => {
        res.push({
          id: item.cid,
          name_zh: item.name_zh,
          name_en: item.name_en,
          intro: item.intro,
          pre_course: item.pre_course,
          textbooks: item.textbooks,
          semester: item.semester,
          teachers: item.teachers,
        });
      });
      return res;
    },
    adminAllTeachers(state) {
      return memberFilter(state.allTeachers);
    },
    adminAllStudents(state) {
      return memberFilter(state.allStudents);
    },
  },
  mutations: {
    initAllCourses(state, { courses }) {
      state.allCourses.splice(0, state.allCourses.length);
      state.allCourses.push(...courses);
    },
    initAllTeachers(state, { teachers }) {
      state.allTeachers.splice(0, state.allTeachers.length);
      state.allTeachers.push(...teachers);
    },
    initAllStudents(state, { students }) {
      state.allStudents.splice(0, state.allStudents.length);
      state.allStudents.push(...students);
    },
  },
  actions: {
    initAllCourses(context) {
      axios.get('/api/v1/courses')
        .then((res) => {
          console.log('courses request success: ', res);
          return context.commit({
            type: 'initAllCourses',
            courses: res.data,
          });
        });
    },
    initAllTeachers(context) {
      axios.get('/api/v1/users/teachers')
        .then((res) => {
          console.log('teachers request success: ', res);
          return context.commit({
            type: 'initAllTeachers',
            teachers: res.data,
          });
        });
    },
    initAllStudents(context) {
      axios.get('/api/v1/users/students')
        .then((res) => {
          console.log('students request success: ', res);
          return context.commit({
            type: 'initAllStudents',
            students: res.data,
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
