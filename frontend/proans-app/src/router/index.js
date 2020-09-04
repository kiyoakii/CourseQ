import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/proans/course/:cid/unAuth',
    name: 'UnAuthView',
    component: () => import('@/views/UnAuthView.vue'),
  },
  {
    path: '/proans/course/:cid',
    name: 'IntroView',
    component: () => import('@/views/GuideView.vue'),
  },
  {
    path: '/proans/course/:cid/tag/:tid',
    name: 'CategoryView',
    component: () => import('@/views/GuideView.vue'),
  },
  {
    path: '/proans/course/:cid/tag/:tid/question/:qid',
    name: 'ProblemView',
    component: () => import('@/views/ProblemView.vue'),
  },
  {
    path: '/proans/course/:cid/tag/:tid/question/:qid/editProblem',
    name: 'EditProblemView',
    component: () => import('@/components/ProblemEdit.vue'),
  },
  {
    path: '/proans/course/:cid/tag/:tid/addProblem',
    name: 'AddProblemView',
    component: () => import('@/components/ProblemEdit.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
