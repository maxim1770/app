<template>
  <v-chip
    variant="text"
  >
    л. {{ first_page.num }}.
  </v-chip>
</template>

<script>


export default {
  props: {
    first_page: {
      type: Object,
      required: true
    }
  }
};

</script>



