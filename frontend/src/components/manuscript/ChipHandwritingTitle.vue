<template>
  <v-chip
    variant="tonal"
    color="red-accent-4"
    prepend-icon="mdi-pencil-outline"
  >
    {{ manuscript.handwriting_title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



