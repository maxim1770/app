<template>
  <component
    :is="bookSource"
    :book="book"
  />
</template>

<script>


import ZachaloBookSource from "@/components/book/book_source_factory/ZachaloBookSource.vue";
import CathedralBookSource from "@/components/book/book_source_factory/CathedralBookSource.vue";
import HolidayBookSource from "@/components/book/book_source_factory/HolidayBookSource.vue";
import BookAuthorSource from "@/components/book/book_source_factory/BookAuthorSource.vue";

export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    bookSource() {
      if (this.book?.zachalo || this.book?.psaltyr_book) {
        return ZachaloBookSource;
      } else if (this.book?.cathedral_book) {
        return CathedralBookSource;
      } else if (this.book?.holiday_book || this.book?.molitva_book) {
        return HolidayBookSource;
      } else if (this.book?.topic_book || this.book?.movable_date_book) {
        return BookAuthorSource;
      }
    }
  }
};
</script>


