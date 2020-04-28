import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);

const routes = [
  {
    path: '/teacher',
    name: 'Teacher',
    redirect: '/teacher/course-list',
  },
  {
    // just for development, we are using dynamic route soon
    path: '/teacher/course-list',
    name: 'CourseList',
    components: {
      header: () => import('../components/TeacherNavBar.vue'),
      content: () => import('../components/TeacherCourseList.vue'),
    },
  },
  {
    path: '/teacher/semester-list',
    name: 'SemesterList',
    components: {
      header: () => import('../components/TeacherNavBar.vue'),
      content: () => import('../components/TeacherSemesterList.vue'),
    },
  },
  {
    path: '/teacher/course',
    name: 'CourseList',
    components: {
      sidebar: () => import('../components/SideBar.vue'),
      header: () => import('../components/TeacherNavBar.vue'),
      content: () => import('../views/CourseIntro.vue'),
    },
  },
  {
    path: '/admin',
    name: 'Admin',
    redirect: '/admin/course-manage',
  },
  {
    path: '/admin/course-manage',
    name: 'CourseManage',
    components: {
      header: () => import('../components/AdminNavBar.vue'),
      content: () => import('../views/AdminCourseManage.vue'),
    },
  },
  {
    path: '/admin/teacher-manage',
    name: 'TeacherManage',
    components: {
      header: () => import('../components/AdminNavBar.vue'),
      content: () => import('../views/AdminTeacherManage.vue'),
    },
  },
  {
    path: '/admin/student-manage',
    name: 'StudentManage',
    components: {
      header: () => import('../components/AdminNavBar.vue'),
      content: () => import('../views/AdminStudentManage.vue'),
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
