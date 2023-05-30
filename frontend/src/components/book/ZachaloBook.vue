<template>
  <v-chip>
    {{ book }}
  </v-chip>
</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>



