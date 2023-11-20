<template>
  <v-list-item
    v-if="movable_date_book?.id"
    :to="{ name: 'book', params: { bookId: movable_date_book.id } }"
  >
    <template v-slot:prepend>
      <v-icon
        icon="mdi-book-heart-outline"
        color="red-darken-4"
      />
    </template>
    <BookmarkPageData :bookmark="bookmark" />
    <MovableDateBookFullTitle :book="movable_date_book.book" :movable_date_book="movable_date_book" />
  </v-list-item>
</template>

<script>


import HolidayBookFullTitle from "@/components/book/book_full_title/HolidayBookFullTitle.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";
import MovableDateBookFullTitle from "@/components/book/book_full_title/MovableDateBookFullTitle.vue";

export default {
  components: { MovableDateBookFullTitle, BookmarkPageData, HolidayBookFullTitle },
  props: {
    movable_date_book: {
      type: Object,
      required: true
    }
  },
  computed: {
    bookmark() {
      return this.movable_date_book?.book?.bookmarks?.[0];
    }
  }
};

</script>



