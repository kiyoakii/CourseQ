import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/proans/:paid/problem/:pid',
    name: 'ProblemView',
    component: () => import('@/views/ProblemView.vue'),
  },
  {
    path: '/proans/:paid/category/:cid/problem/:pid',
    name: 'CategoryView',
    component: () => import('@/views/ProblemView.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
