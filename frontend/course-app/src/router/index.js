import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import CourseRes from '@/views/CourseRes.vue';
import CourseCalendar from '@/views/CourseCalendar.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/:cid/home',
    name: 'Home',
    component: Home,
  },
  {
    path: '/:cid',
    redirect: '/:cid/home',
  },
  {
    path: '/:cid/resourse',
    name: 'CourseRes',
    component: CourseRes,
  },
  {
    path: '/:cid/calendar',
    name: 'CourseCalendar',
    component: CourseCalendar,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: 'course',
  routes,
});

export default router;
