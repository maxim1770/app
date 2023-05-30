const dateRoutes = [
  {
    path: '/dates', name: 'dates', component: () => import('@/views/DatesView.vue'),
  }, {
    path: '/dates/:date', name: 'date', component: () => import('@/views/DateView.vue'),
  },
]

export default dateRoutes;