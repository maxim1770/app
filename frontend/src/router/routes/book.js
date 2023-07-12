const bookRoutes = [
  {
    path: "/books", name: "books", component: () => import("@/views/BooksView.vue")
  }, {
    path: "/books/:bookId", name: "book", component: () => import ("@/views/BookView.vue")
  }, {
    path: "/books/cathedrals", name: "cathedrals", component: () => import ("@/views/CathedralsView.vue")
  }, {
    path: "/books/bible-books", name: "bible-books", component: () => import ("@/views/BibleBooksView.vue")
  }, {
    path: "/books/lls", name: "lls", component: () => import ("@/views/LlsView.vue")
  }
];

export default bookRoutes;