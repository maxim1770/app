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
  head: {
    title: "My awesome site"
  },
  metaInfo: {
    htmlAttrs: {
      lang: "ru-RU",
      amp: true
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1.0" }
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
  setup() {
    // const head = useHead();
    // head.title.value = "Православие в Рукописях";
    // head.meta.description = "Выдержки из Рукописей до 1597 года";
    // head.link.icon = "/FaviconOrthodoxCross.ico";
    // return { head };
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

