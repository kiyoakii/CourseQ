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
    name: 'TeacherCourseManage',
    components: {
      sidebar: () => import('../components/SideBar.vue'),
      header: () => import('../components/TeacherNavBar.vue'),
      content: () => import('../views/TeacherCourseManage.vue'),
    },
    redirect: '/teacher/course/assistants',
    children: [
      {
        path: 'assistants',
        component: () => import('../views/TeacherAssiList.vue'),
      },
      {
        path: 'students',
        component: () => import('../views/StudentList.vue'),
      },
      {
        path: 'intro',
        component: () => import('../views/CourseIntro.vue'),
      },
      {
        path: 'announce',
        component: () => import('../views/CourseAnnounce.vue'),
      },
      {
        path: 'assignment',
        component: () => import('../views/CourseAssignment.vue'),
      },
      {
        path: 'resource',
        component: () => import('../views/CourseRes.vue'),
      },
      {
        path: 'schedule',
        component: () => import('../views/CourseSchedule.vue'),
      },
      {
        path: 'teacher',
        component: () => import('../views/TeacherInfo.vue'),
      },
    ],
  },
  {
    path: '/admin',
    name: 'Admin',
    redirect: '/admin/course-manage',
  },
  {
    path: '/admin/course-manage',
    name: 'AdminCourseManage',
    components: {
      header: () => import('../components/AdminNavBar.vue'),
      content: () => import('../views/AdminCourseManage.vue'),
    },
  },
  {
    path: '/admin/teacher-manage',
    name: 'AdminTeacherManage',
    components: {
      header: () => import('../components/AdminNavBar.vue'),
      content: () => import('../views/AdminTeacherManage.vue'),
    },
  },
  {
    path: '/admin/student-manage',
    name: 'AdminStudentManage',
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
