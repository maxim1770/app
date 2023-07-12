import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import vuetify from "@/plugins/vuetify/vuetify";
import VCalendar from "v-calendar";
import "moment/locale/ru";
import moment from "moment";
import "v-calendar/style.css";
import VueViewer from "v-viewer";

moment.locale("ru");

const app = createApp(App);

app.use(VueViewer.default)

app.use(router).use(vuetify);

app.use(VCalendar, {
  locale: "ru",
  popoverVisibility: "focus",
  firstDayOfWeek: 1,
  datePickerTintColor: "#4CAF50"
});

app.config.globalProperties.$moment = moment;

app.mount("#app");
