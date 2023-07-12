<template>
  <v-chip
    :to="{ name: 'book', params: { bookId: zachalo.id } }"
    :color="color"
    prepend-icon="mdi-book-open-page-variant"
  >
    {{ zachalo.bible_book.abbr_ru }} зач. {{ zachalo.num }}
  </v-chip>
</template>

<script>


export default {
  props: {
    zachalo: {
      type: Object,
      required: true
    },
    color: {
      type: Object,
      required: false,
      default: "success"
    }
  }
};

</script>



