<template>
  <v-list-item
    v-if="holiday_book?.id"
    :to="{ name: 'book', params: { bookId: holiday_book.id } }"
  >
    <template v-slot:prepend>
      <v-icon
        icon="mdi-book-heart-outline"
        :color="choiceHolidayColor(Holiday)"
      />
    </template>
    <BookmarkPageData :bookmark="bookmark" />
    <HolidayBookFullTitle
      :book="holiday_book.book"
      :holiday_book="holiday_book"
      :holiday="holiday"
      :saint="saint"
    />
  </v-list-item>
</template>

<script>


import HolidayBookFullTitle from "@/components/book/book_full_title/HolidayBookFullTitle.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";
import { choiceHolidayColor } from "@/utils/holidays";

export default {
  components: { BookmarkPageData, HolidayBookFullTitle },
  props: {
    holiday_book: {
      type: Object,
      required: true
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    },
    saint: {
      type: Object,
      required: false,
      default: null
    }
  },
  computed: {
    bookmark() {
      return this.holiday_book.book.bookmarks?.[0];
    },
    Holiday() {
      return this.holiday ? this.holiday : this.holiday_book?.holiday;
    }
  },
  methods: { choiceHolidayColor }
};

</script>



