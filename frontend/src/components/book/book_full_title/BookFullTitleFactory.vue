<template>
  <component
    :is="bookFullTitle"
    :book="book"
  />
</template>

<script>


import HolidayBookFullTitle from "@/components/book/book_full_title/HolidayBookFullTitle.vue";
import TopicBookFullTitle from "@/components/book/book_full_title/TopicBookFullTitle.vue";
import MolitvaBookFullTitle from "@/components/book/book_full_title/MolitvaBookFullTitle.vue";
import MovableDateBookFullTitle from "@/components/book/book_full_title/MovableDateBookFullTitle.vue";
import ZachaloBookFullTitle from "@/components/book/book_full_title/ZachaloBookFullTitle.vue";
import CathedralBookFullTitle from "@/components/book/book_full_title/CathedralBookFullTitle.vue";
import LlsBookFullTitle from "@/components/book/book_full_title/LlsBookFullTitle.vue";
import SomeBookFullTitle from "@/components/book/book_full_title/SomeBookFullTitle.vue";
import PsaltyrBookFullTitle from "@/components/book/book_full_title/PsaltyrBookFullTitle.vue";

export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    bookFullTitle() {
      if (this.book?.holiday_book) {
        return HolidayBookFullTitle;
      } else if (this.book?.topic_book) {
        return TopicBookFullTitle;
      } else if (this.book?.molitva_book) {
        return MolitvaBookFullTitle;
      } else if (this.book?.movable_date_book) {
        return MovableDateBookFullTitle;
      } else if (this.book?.zachalo) {
        return ZachaloBookFullTitle;
      } else if (this.book?.cathedral_book) {
        return CathedralBookFullTitle;
      } else if (this.book?.psaltyr_book) {
        return PsaltyrBookFullTitle;
      } else if (this.book?.lls_book) {
        return LlsBookFullTitle;
      } else {
        return SomeBookFullTitle;
      }
    }
  }
};
</script>

