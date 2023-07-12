<template>
  <v-chip>
    {{ book?.bookmark_title }}
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



