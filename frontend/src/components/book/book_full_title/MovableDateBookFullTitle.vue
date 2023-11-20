<template>
  <v-chip
    color="pink-darken-1"
    class="ma-1"
  >
    {{ book.type }}
  </v-chip>
  <BookAuthor :saint="book.author" />
  <v-chip
    color="pink-darken-1"
    class="ma-1"
  >
    в
  </v-chip>
  <ChipMovableDay
    :movable_day="movableDateBook?.movable_day"
    class="ma-1"
  />
</template>

<script>


import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";
import BookAuthor from "@/components/book/book_full_title/__BookAuthor.vue";

export default {
  components: { BookAuthor, ChipMovableDay },
  props: {
    book: {
      type: Object,
      required: true
    },
    movable_date_book: {
      type: Object,
      required: false,
      default: null
    }
  },
  computed: {
    movableDateBook() {
      return this.movable_date_book ? this.movable_date_book : this.book.movable_date_book;
    }
  }
};

</script>



