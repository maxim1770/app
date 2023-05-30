import { createRouter, createWebHistory } from "vue-router";
import holidayRoutes from "@/router/routes/holiday";
import saintRoutes from "@/router/routes/saint";
import bookRoutes from "@/router/routes/book";
import dateRoutes from "@/router/routes/date";
import manuscriptRoutes from "@/router/routes/manuscript";
import movableDateRoutes from "@/router/routes/movableDate";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/", name: "home", component: () => import("@/views/HomeView.vue")
    },
    ...holidayRoutes,
    ...saintRoutes,
    ...dateRoutes,
    ...movableDateRoutes,
    ...manuscriptRoutes,
    ...bookRoutes
  ]
});

export default router;