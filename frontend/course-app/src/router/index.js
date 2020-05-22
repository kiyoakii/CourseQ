import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '@/views/Home.vue';
import CourseRes from '@/views/CourseRes.vue';
import CourseCalendar from '@/views/CourseCalendar.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/course/:cid/semester/:sid/home',
    name: 'Home',
    component: Home,
    alias: '/course/:cid/semester/:sid',
  },
  {
    path: '/course/:cid/semester/:sid/course-res',
    name: 'CourseRes',
    component: CourseRes,
  },
  {
    path: '/course/:cid/semester/:sid/course-calendar',
    name: 'CourseCalendar',
    component: CourseCalendar,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
