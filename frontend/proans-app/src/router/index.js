import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/proans/problem/:pid',
    name: 'ProblemView',
    component: () => import('@/views/ProblemView.vue'),
  },
  {
    path: '/proans/',
    name: 'CategoryView',
    components: {
      default: () => import('@/views/ProblemView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
