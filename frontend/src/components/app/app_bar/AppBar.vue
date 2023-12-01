<template>
  <NavigationDrawer
    :mainData="mainData"
    :drawer=drawer
    @update:drawer="drawer = !drawer"
  />
  <v-app-bar>
    <AppBarTitle v-once />
    <AppBarAppend
      :mainData="mainData"
      @update:drawer="drawer = !drawer"
    />
  </v-app-bar>
</template>

<script>


import AppBarDate from "@/components/date/AppBarDate.vue";
import AppBarTitle from "@/components/app/app_bar/AppBarTitle.vue";
import AppBarAppend from "@/components/app/app_bar/AppBarAppend.vue";
import NavigationDrawer from "@/components/app/app_bar/navigation_drawer/NavigationDrawer.vue";
import { mainPages } from "@/utils/common";

export default {
  components: { NavigationDrawer, AppBarAppend, AppBarTitle, AppBarDate },
  props: {
    mainData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      drawer: null
    };
  },
  computed: {
    mainPages() {
      return mainPages;
    }
  }
};

</script>



