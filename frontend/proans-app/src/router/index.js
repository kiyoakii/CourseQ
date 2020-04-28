import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    // c_id: category_id, p_id: problem_id
    path: '/:c_id/:p_id/answer',
    name: 'Answer',
    component: () => import('../views/AnswerView.vue'),
    alias: '/:c_id/:p_id',
  },
  {
    // c_id: category_id, p_id: problem_id
    path: '/:c_id/:p_id/timeline',
    name: 'TimeLine',
    component: () => import('../views/TimeLine.vue'),
  },
  {
    // c_id: category_id, p_id: problem_id
    path: '/:c_id/:p_id/editor',
    name: 'Editor',
    component: () => import('../views/Editor.vue'),
  },
];

const router = new VueRouter({
  routes,
});

export default router;
