const saintRoutes = [
  {
    path: '/saints', name: 'saints', component: () => import('@/views/SaintsView.vue'),
  }, {
    path: '/saints/:saintSlug', name: 'saint', component: () => import('@/views/SaintView.vue'),
  }
]

export default saintRoutes;