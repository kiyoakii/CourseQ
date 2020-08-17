import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/proans/course/:cid',
    name: 'IntroView',
    components: {
      default: () => import('@/views/GuideView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/course/:cid/tag/:tid',
    name: 'CategoryView',
    components: {
      default: () => import('@/views/GuideView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/course/:cid/tag/:tid/question/:qid',
    name: 'ProblemView',
    components: {
      default: () => import('@/views/ProblemView.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/course/:cid/tag/:tid/question/:qid/editProblem',
    name: 'EditProblemView',
    components: {
      default: () => import('@/components/ProblemEdit.vue'),
      sidebar: () => import('@/components/SideBar.vue'),
    },
  },
  {
    path: '/proans/course/:cid/tag/:tid/addProblem',
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
