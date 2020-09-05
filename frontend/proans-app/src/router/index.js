import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/course/:cid/unAuth',
    name: 'UnAuthView',
    component: () => import('@/views/UnAuthView.vue'),
  },
  {
    path: '/course/:cid',
    name: 'IntroView',
    redirect: '/course/:cid/tag/all',
    component: () => import('@/views/GuideView.vue'),
  },
  {
    path: '/course/:cid/tag/:tid',
    name: 'CategoryView',
    component: () => import('@/views/GuideView.vue'),
  },
  {
    path: '/course/:cid/tag/:tid/question/:qid',
    name: 'ProblemView',
    component: () => import('@/views/ProblemView.vue'),
  },
  {
    path: '/course/:cid/tag/:tid/question/:qid/editProblem',
    name: 'EditProblemView',
    component: () => import('@/components/ProblemEdit.vue'),
  },
  {
    path: '/course/:cid/tag/:tid/addProblem',
    name: 'AddProblemView',
    component: () => import('@/components/ProblemEdit.vue'),
  },
];

const router = new VueRouter({
  mode: 'history',
  base: 'proans',
  routes,
});

export default router;
