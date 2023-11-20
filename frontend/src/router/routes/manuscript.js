const manuscriptRoutes = [{
  path: "/manuscripts", name: "manuscripts", component: () => import("@/views/ManuscriptsView.vue")
}, {
  path: "/manuscripts/:manuscriptCode", name: "manuscript", component: () => import("@/views/ManuscriptView.vue")
}, {
  path: "/manuscripts/lls", name: "lls", component: () => import ("@/views/LlsView.vue")
}
];

export default manuscriptRoutes;