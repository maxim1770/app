const iconRoutes = [{
  path: "/icons/:iconId", name: "icon", component: () => import("@/views/IconView.vue")
}];

export default iconRoutes;