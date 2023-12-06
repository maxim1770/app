<template>
  <v-app>
    <AppBar
      v-memo="[mainData?.date?.day?.id]"
      :mainData="mainData"
    />
    <AppMain />
  </v-app>
</template>

<script>
import { api } from "@/services/api";
import AppBar from "@/components/app/app_bar/AppBar.vue";
import AppMain from "@/components/app/app_main/AppMain.vue";
import { mainPages } from "@/utils/common";

export default {
  metaInfo: {
    title: "Православие в Рукописях",
    titleTemplate: "%s | Православие в Рукописях",
    htmlAttrs: {
      lang: "ru-RU",
      amp: true
    },
    meta: [
      { charset: "utf-8" },
      { vmid: "description", name: "description", content: "Выдержки из Рукописей до 1597 года" },
      { name: "viewport", content: "width=device-width, initial-scale=1.0" }
    ],
    link: [
      { rel: "icon", href: "/FaviconOrthodoxCross.ico" }
    ]
  },
  components: { AppMain, AppBar },
  data() {
    return {
      mainData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getMainData()
      .then((response) => (this.mainData = response.data));
  },
  computed: {
    mainPages() {
      return mainPages;
    }
  }
};
</script>

