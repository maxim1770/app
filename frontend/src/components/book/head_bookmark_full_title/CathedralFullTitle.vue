<template>
  {{ cathedral.title }} (Кол. Правил
  <v-chip
    variant="tonal"
    color="blue"
  >
    {{ cathedral.num_rules }}
  </v-chip>
  )

</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    cathedral() {
      return this.book.cathedral_book.cathedral;
    }
  }
};

</script>



