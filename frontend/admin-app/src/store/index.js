import Vue from 'vue';
import Vuex from 'vuex';
import VuexPersistence from 'vuex-persist';
import axios from 'axios';
import {
  memberFilter,
  courseFilter,
  teacherOptionsFilter,
  distinctCoursesFilter,
} from '../helpers/filters';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    allCourses: [],
    allTeachers: [],
    allStudents: [],
    courses: [],
  },
  getters: {
    adminAllCourses(state) {
      return courseFilter(state.allCourses);
    },
    adminAllTeachers(state) {
      return memberFilter(state.allTeachers);
    },
    adminAllStudents(state) {
      return memberFilter(state.allStudents);
    },
    teacherOptions(state) {
      return teacherOptionsFilter(state.allTeachers);
    },
    getCourseByID(state) {
      return (id) => {
        return state.allCourses.find((course) => {
          return course.cid === id;
        });
      };
    },
    teacherCourses(state) {
      return state.courses;
    },
    courseAllInfo(state) {
      return (cid) => {
        return state.courses.find((item) => String(item.cid) === String(cid));
      };
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
    initCourses(state, { courses }) {
      state.courses.splice(0, state.courses.length);
      state.courses.push(...courses);
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
    initCourses(context, { tid }) {
      axios.get(`/api/v1/users/${tid}/courses`)
        .then((res) => {
          console.log('courses get: ', res);
          return context.commit({
            type: 'initCourses',
            courses: res.data,
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
