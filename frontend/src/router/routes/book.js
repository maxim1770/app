const bookRoutes = [{
  path: "/books", name: "books", component: () => import("@/views/BooksView.vue")
}, {
  path: "/books/:bookId", name: "book", component: () => import ("@/views/BookView.vue")
}, {
  path: "/books/cathedrals", name: "cathedrals", component: () => import ("@/views/CathedralsView.vue")
}, {
  path: "/books/cathedrals/:cathedralSlug", name: "cathedral", component: () => import ("@/views/cathedral/CathedralMainView.vue")
}, {
  path: "/books/bible-books", name: "bible-books", component: () => import ("@/views/BibleBooksView.vue")
}, {
  path: "/books/bible-books/:bibleBookAbbr", name: "bible-book", component: () => import ("@/views/bible_book/BibleBookMainView.vue")
}];

export default bookRoutes;