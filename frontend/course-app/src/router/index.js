import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/course-res',
    name: 'CourseRes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/CourseRes.vue'),
  },
  {
    path: '/course-calendar',
    name: 'CourseCalendar',
    component: () => import('../views/CourseCalendar.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
