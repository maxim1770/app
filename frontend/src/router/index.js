import {createRouter, createWebHistory} from 'vue-router';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/HomeView.vue'),
    },
    {
      path: '/dates',
      name: 'dates',
      component: () => import('@/views/DatesView.vue'),
    },
    {
      path: '/dates/:date',
      name: 'date',
      component: () => import('@/views/DateView.vue'),
    },
    {
      path: '/movable-dates/cycle-:cycleNum(\\d+)',
      name: 'cycle',
      component: () => import('@/views/CycleView.vue'),
    },
    {
      path: '/holidays',
      name: 'holidays',
      component: () => import('@/views/HolidaysView.vue'),
    },
    {
      path: '/holidays/:holidaySlug',
      name: 'holiday',
      component: () => import('@/views/HolidayView.vue'),
    },
    {
      path: '/saints/:saintSlug',
      name: 'saint',
      component: () => import('@/views/SaintView.vue'),
    },
    {
      path: '/manuscripts',
      name: 'manuscripts',
      component: () => import('@/views/ManuscriptsView.vue'),
    },
  ],
});

export default router;
