<template>
  <v-chip
    variant="tonal"
    color="blue"
  >
    {{ dignity.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    dignity: {
      type: Object,
      required: true
    }
  }
};

</script>



