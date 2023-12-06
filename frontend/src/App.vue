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

