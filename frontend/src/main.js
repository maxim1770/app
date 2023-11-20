import { createApp } from "vue";
import App from "@/App.vue";
import router from "@/router";
import vuetify from "@/plugins/vuetify/vuetify";
import VCalendar from "v-calendar";
import "moment/locale/ru";
import moment from "moment";
import "v-calendar/style.css";
import VueViewer from "v-viewer";
import "viewerjs/dist/viewer.css";


const app = createApp(App);

moment.locale("ru");
app.config.globalProperties.$moment = moment;

app.use(router).use(vuetify);
app.use(VCalendar, {
  locale: "ru", popoverVisibility: "focus", firstDayOfWeek: 1, datePickerTintColor: "#4CAF50"
});
app.use(VueViewer);
app.mount("#app");
