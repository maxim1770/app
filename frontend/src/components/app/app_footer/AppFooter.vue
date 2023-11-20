<template>
  <v-footer class="bg-grey-lighten-1 text-center d-flex flex-column">
    <v-row justify="center" no-gutters>
      <v-btn
        v-for="mainPage in mainPages"
        :key="mainPage"
        @click="$router.push({ name: mainPage.value })"
        color="white"
        variant="text"
        class="mx-2"
        rounded="xl"
        :prepend-icon="mainPage.prependIcon"
      >
        {{ mainPage.title }}
      </v-btn>
      <v-col class="text-center mt-4">
        {{ mainData.date.year }} — <strong>Православие в Рукописях</strong>
      </v-col>
    </v-row>
  </v-footer>
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



