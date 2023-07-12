<template>
  <v-chip
    variant="tonal"
    color="red"
    :prepend-icon="`custom:${tipikon.title_en.replace('_', '')}`"
  >
    {{ tipikon.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    tipikon: {
      type: Object,
      required: true
    }
  }
};

</script>



