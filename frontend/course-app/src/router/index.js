import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import CourseRes from '@/views/CourseRes.vue';
import CourseCalendar from '@/views/CourseCalendar.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/course/:cid/home',
    name: 'Home',
    component: Home,
    alias: '/course/:cid',
  },
  {
    path: '/course/:cid/resourse',
    name: 'CourseRes',
    component: CourseRes,
  },
  {
    path: '/course/:cid/calendar',
    name: 'CourseCalendar',
    component: CourseCalendar,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
