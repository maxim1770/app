import { createRouter, createWebHistory } from "vue-router";
import holidayRoutes from "@/router/routes/holiday";
import saintRoutes from "@/router/routes/saint";
import bookRoutes from "@/router/routes/book";
import dateRoutes from "@/router/routes/date";
import manuscriptRoutes from "@/router/routes/manuscript";
import movableDateRoutes from "@/router/routes/movableDate";
import iconRoutes from "@/router/routes/icon";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), routes: [{
    path: "/", name: "main", component: () => import("@/views/MainView.vue")
  }, ...holidayRoutes, ...saintRoutes, ...dateRoutes, ...movableDateRoutes, ...manuscriptRoutes, ...bookRoutes, ...iconRoutes],
  scrollBehavior(to, from, savedPosition) {
    if (from.path !== to.path) {
      document.getElementById("app").scrollIntoView({ behavior: "smooth" });
    }
  }
});

export default router;