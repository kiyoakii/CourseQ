import Vue from 'vue';
import VueRouter from 'vue-router';
import SignIn from '@/views/SignIn.vue';
import Profile from '@/views/Profile.vue';
import VueContent from '@/views/VueContent.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Content',
    component: VueContent,
    children: [
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
    ],
  },
  {
    path: '/signin',
    name: 'SignIn',
    component: SignIn,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
