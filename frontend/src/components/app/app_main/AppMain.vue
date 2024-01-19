<template>
  <v-main>
    <v-container
      class="d-flex justify-center align-center"
      style="min-height: 300px;"
    >
      <router-view />
      <ScrollUp v-once />
    </v-container>
  </v-main>
</template>

<script>


import ScrollUp from "@/components/common/ScrollUp.vue";

export default {
  components: { ScrollUp }
};

</script>
