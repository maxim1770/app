<template>
  <v-chip
    v-if="book && book.title.includes('толк')"
    :to="{ name: 'book', params: { bookId: book.id } }"
    prepend-icon="mdi-check-circle-outline"
    color="blue"
    class="ma-1"
  >
    Толковое
  </v-chip>
  <ChipZachalo
    :zachalo="book.zachalo"
    :hasBibleBookLink="true"
    :hasAlwaysSeeOptional="true"
  />
</template>

<script>


import ChipZachalo from "@/components/book/ChipZachalo.vue";

export default {
  components: { ChipZachalo },
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>

