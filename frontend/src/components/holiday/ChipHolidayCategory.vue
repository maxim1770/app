<template>
  <v-chip
    variant="tonal"
    color="green"
  >
    {{ holiday_category?.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    holiday_category: {
      type: Object,
      required: true
    }
  }
};

</script>






