import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/proans/',
    name: 'IntroView',
    components: {
      default: () => import('@/views/GuideView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/',
    name: 'ProblemView',
    components: {
      default: () => import('@/views/ProblemView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/',
    name: 'CategoryView',
    components: {
      default: () => import('@/views/GuideView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/editProblem',
    name: 'EditProblemView',
    components: {
      default: () => import('@/components/ProblemEdit.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/addProblem',
    name: 'AddProblemView',
    components: {
      default: () => import('@/components/ProblemEdit.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
