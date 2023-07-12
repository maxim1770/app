<template>
  <v-chip
    v-if="book.title.includes('толковое')"
    variant="tonal"
    color="green"
  >
    Толковое
  </v-chip>
  <v-chip class="ml-1">
    {{ book.zachalo.bible_book.title }} зачало {{ book.zachalo.num }}
  </v-chip>
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



