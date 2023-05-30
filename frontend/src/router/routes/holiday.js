const holidayRoutes = [
  {
    path: '/holidays', name: 'holidays', component: () => import('@/views/HolidaysView.vue'),
  }, {
    path: '/holidays/:holidaySlug', name: 'holiday', component: () => import('@/views/HolidayView.vue'),
  }
]

export default holidayRoutes;