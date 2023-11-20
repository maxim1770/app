<template>
  <v-chip
    v-if="city"
    color="amber-darken-2"
    prepend-icon="mdi-map-marker-outline"
  >
    {{ city.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    city: {
      type: Object,
      required: true
    }
  }
};

</script>



