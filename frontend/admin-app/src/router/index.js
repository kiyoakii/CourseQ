import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);

const routes = [
  {
    path: '/teacher/:tid',
    name: 'TeacherView',
    component: () => import('@/views/teacher/TeacherView.vue'),
    children: [
      {
        path: 'courses',
        name: 'TeacherCourseList',
        component: () => import('@/views/teacher/CourseListView.vue'),
      },
      {
        path: 'course/:cid/semesters',
        name: 'TeacherSemesterList',
        component: () => import('@/views/teacher/SemesterListView.vue'),
      },
      {
        path: '/teacher/:tid/course/:cid/semester/:sid/manage',
        name: 'TeacherCourseManage',
        component: () => import('@/views/teacher/ManageView.vue'),
        redirect: '/teacher/:tid/course/:cid/semester/:sid/manage/assistants',
        children: [
          {
            path: 'assistants',
            component: () => import('@/views/teacher/manage/TeacherAssiList.vue'),
          },
          {
            path: 'students',
            component: () => import('@/views/teacher/manage/StudentList.vue'),
          },
          {
            path: 'intro',
            component: () => import('@/views/teacher/manage/CourseIntro.vue'),
          },
          {
            path: 'announce',
            component: () => import('@/views/teacher/manage/CourseAnnounce.vue'),
          },
          {
            path: 'assignment',
            component: () => import('@/views/teacher/manage/CourseAssignment.vue'),
          },
          {
            path: 'resource',
            component: () => import('@/views/teacher/manage/CourseRes.vue'),
          },
          {
            path: 'schedule',
            component: () => import('@/views/teacher/manage/CourseSchedule.vue'),
          },
          {
            path: 'teacher',
            component: () => import('@/views/teacher/manage/TeacherInfo.vue'),
          },
        ],
      },
    ],
  },
  // {
  //   path: '/admin',
  //   name: 'Admin',
  //   redirect: '/admin/course-manage',
  // },
  // {
  //   path: '/admin/course-manage',
  //   name: 'AdminCourseManage',
  //   components: {
  //     header: () => import('../components/AdminNavBar.vue'),
  //     content: () => import('../views/AdminCourseManage.vue'),
  //   },
  // },
  // {
  //   path: '/admin/teacher-manage',
  //   name: 'AdminTeacherManage',
  //   components: {
  //     header: () => import('../components/AdminNavBar.vue'),
  //     content: () => import('../views/AdminTeacherManage.vue'),
  //   },
  // },
  // {
  //   path: '/admin/student-manage',
  //   name: 'AdminStudentManage',
  //   components: {
  //     header: () => import('../components/AdminNavBar.vue'),
  //     content: () => import('../views/AdminStudentManage.vue'),
  //   },
  // },
];

const router = new VueRouter({
  routes,
});

export default router;
