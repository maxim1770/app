<template>
  <v-chip
    variant="tonal"
    color="blue"
    prepend-icon="mdi-timer-sand"
  >
    {{ year?.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    year: {
      type: Object,
      required: true
    }
  }
};

</script>



