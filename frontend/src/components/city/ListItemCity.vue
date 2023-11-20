<template>
  <v-list-item
    v-if="city"
    prepend-icon="mdi-map-marker-outline"
  >
    Город, Страна
    <ChipCity :city="city" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipCity from "@/components/city/ChipCity.vue";

export default {
  components: { ChipCity },
  props: {
    city: {
      type: Object,
      required: true
    }
  }
};

</script>



