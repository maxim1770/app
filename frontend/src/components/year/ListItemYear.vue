<template>
  <v-list-item
    prepend-icon="mdi-timer-sand"
  >
    Год:
    <v-chip
      variant="tonal"
      color="blue"
      class="ml-1"
    >
      {{ year?.title }}
    </v-chip>
  </v-list-item>
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



