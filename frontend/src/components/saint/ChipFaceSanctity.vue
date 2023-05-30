<template>
  <v-chip
    variant="tonal"
    color="green"
  >
    {{ face_sanctity.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    face_sanctity: {
      type: Object,
      required: true
    }
  }
};

</script>



