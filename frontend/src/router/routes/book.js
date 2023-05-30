const bookRoutes = [
  {
    path: '/books', name: 'books', component: () => import('@/views/BooksView.vue'),
  }, {
    path: '/books/:bookId', name: 'book', component: () => import ('@/views/BookView.vue'),
  },
]

export default bookRoutes;