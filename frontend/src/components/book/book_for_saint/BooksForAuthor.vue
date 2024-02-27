<template>
  <ChapterWithHead
    v-if="books?.length || bible_books.length"
    headTitle="Труды"
  >
    <template
      v-if="bible_books.length"
    >
      <ImgMainTitle
        mainPageValue="bible-books"
        @click="$router.push({ name: 'bible-books' })"
      />
      <v-divider />
      <TimelineBibleBooks
        :bible_books="bible_books"
      />
      <v-divider class="mb-6" />
    </template>
    <v-card
      v-if="books?.length"
    >
      <v-card-item>
        <v-list>
          <v-list-item
            v-for="book in books"
            :key="book.id"
            :to="{ name: 'book', params: { bookId: book.id } }"
          >
            <template v-slot:prepend>
              <v-icon
                icon="mdi-book-open-page-variant"
                :color="choiceHolidayColor(findBookHoliday(book))"
              />
            </template>
            <BookFullTitleFactory :book="book" />
          </v-list-item>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>

import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import TimelineBibleBooks from "@/components/book/timeline/TimelineBibleBooks.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import { choiceHolidayColor } from "@/utils/holidays";

export default {
  components: { ImgMainTitle, TimelineBibleBooks, BookFullTitleFactory, ChapterWithHead },
  props: {
    books: {
      type: Array,
      required: true
    },
    bible_books: {
      type: Object,
      required: true
    }
  },
  methods: {
    choiceHolidayColor,
    findBookHoliday(book) {
      if (book.holiday_book) {
        return book.holiday_book.holiday;
      } else if (book.molitva_book) {
        return book.molitva_book.holiday;
      } else {
        return null;
      }
    }
  }
};
</script>