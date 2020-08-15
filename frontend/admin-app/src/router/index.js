import Vue from 'vue';
import VueRouter from 'vue-router';


Vue.use(VueRouter);

const routes = [
  {
    path: '/teacher',
    name: 'TeacherView',
    component: () => import('@/views/teacher/TeacherView.vue'),
    redirect: '/teacher/courses',
    children: [
      {
        path: 'courses',
        name: 'TeacherCourseList',
        component: () => import('@/views/teacher/CourseListView.vue'),
      },
      {
        path: 'courses/:cname/semesters',
        name: 'TeacherSemesterList',
        component: () => import('@/views/teacher/SemesterListView.vue'),
      },
      {
        path: '/teacher/courses/:cname/semesters/:sname/manage/:cid',
        name: 'TeacherCourseManage',
        component: () => import('@/views/teacher/ManageView.vue'),
        redirect: '/teacher/courses/:cname/semesters/:sname/manage/:cid/assistants',
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
  {
    path: '/admin/:aid',
    name: 'AdminView',
    component: () => import('@/views/admin/AdminView.vue'),
    redirect: '/admin/:aid/courses',
    children: [
      {
        path: 'courses',
        name: 'AdminCourseManage',
        component: () => import('@/views/admin/CourseManage.vue'),
      },
      {
        path: 'teachers',
        name: 'AdminTeacherManage',
        component: () => import('@/views/admin/TeacherManage.vue'),
      },
      {
        path: 'students',
        name: 'AdminStudentManage',
        component: () => import('@/views/admin/StudentManage.vue'),
      },
    ],
  },
];

const router = new VueRouter({
  routes,
});

export default router;
