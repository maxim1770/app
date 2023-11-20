<template>
  <v-list>
    <v-list-item
      v-for="mainPage in mainPages"
      :key="mainPage.title"
      :to="{ name: mainPage.value }"
      :title="mainPage.title"
      :prepend-icon="mainPage.prependIcon"
      color="blue-lighten-1"
    >
    </v-list-item>
  </v-list>
</template>

<script>


import { mainPages } from "@/utils/common";

export default {
  props: {
    mainData: {
      type: Object,
      required: true
    }
  },
  computed: {
    mainPages() {
      return mainPages;
    }
  }
};

</script>



