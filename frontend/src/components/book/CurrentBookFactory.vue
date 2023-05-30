<template>
  <component
    :is="currentBook"
    :book="book"
  />
</template>

<script>


import HolidayBook from "@/components/book/HolidayBook.vue";
import TopicBook from "@/components/book/TopicBook.vue";
import MolitvaBook from "@/components/book/MolitvaBook.vue";
import MovableDateBook from "@/components/book/MovableDateBook.vue";
import ZachaloBook from "@/components/book/ZachaloBook.vue";

export default {
  components: {
    HolidayBook, TopicBook, MolitvaBook
  },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    currentBook() {
      if (this.book.holiday_book) {
        return HolidayBook;
      } else if (this.book.topic_book) {
        return TopicBook;
      } else if (this.book.molitva_books) {
        return MolitvaBook;
      } else if (this.book.movable_date_book) {
        return MovableDateBook;
      } else if (this.book.zachalo) {
        return ZachaloBook;
      }
    }
  }
};
</script>

