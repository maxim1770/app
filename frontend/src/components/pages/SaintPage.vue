<template>
  <div
    v-memo="[saint?.id]"
  >
    <CarouselMain :imgs_data="allIcons" />
    <MainTitle
      :title="saint.name"
      :textColor="choiceHolidayColor(bestTipikonPriorityHoliday)"
    />
    <SaintData :saint="saint" />
    <ListHolidays :holidays="sortedHolidays" />
    <BooksForHoliday
      :molitva_books_by_manuscript="molitvaBooksByManuscript"
      :holiday_books="allHolidaysBooks"
      :saint="saint"
    />
    <BooksForAuthor :books="booksWithSaint" :bible_books="saint?.bible_books" />
  </div>
</template>

<script>

import MainTitle from "@/components/common/title/MainTitle.vue";
import ListHolidays from "@/components/holiday/ListHolidays.vue";
import SaintData from "@/components/saint/SaintData.vue";
import BooksForAuthor from "@/components/book/book_for_saint/BooksForAuthor.vue";
import CarouselMain from "@/components/gallery/CarouselMain.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import BooksForHoliday from "@/components/book/book_for_holiday/BooksForHoliday.vue";
import { choiceHolidayColor, prepareAllHolidaysBooks, prepareAllIcons, sortHolidays } from "@/utils/holidays";


export default {
  components: {
    BooksForHoliday,
    ChapterWithHead,
    CarouselMain,
    SaintData,
    BooksForAuthor,
    ListHolidays,
    MainTitle
  },
  props: {
    saint: {
      type: Object,
      required: true
    }
  },
  computed: {
    allIcons() {
      return prepareAllIcons(this.sortedHolidays);
    },
    allHolidaysBooks() {
      let allHolidaysBooks = prepareAllHolidaysBooks(this.sortedHolidays);
      if (this.saint.holiday_books.length) {
        allHolidaysBooks = allHolidaysBooks.concat(this.saint.holiday_books);
      }
      return allHolidaysBooks;
    },
    molitvaBooksByManuscript() {
      let molitvaBooksByManuscript = {};
      for (let holiday of this.sortedHolidays) {
        if (holiday.molitva_books_by_manuscript) {
          for (let manuscript_code in holiday.molitva_books_by_manuscript) {
            molitvaBooksByManuscript[holiday.slug + "_" + manuscript_code] = holiday.molitva_books_by_manuscript[manuscript_code];
          }
        }
      }
      return molitvaBooksByManuscript;
    },
    sortedHolidays() {
      return sortHolidays(this.saint.holidays);
    },
    booksWithSaint() {
      let booksWithSaint = [];
      for (let book of this.saint.books) {
        book.author = this.saint;
        booksWithSaint.push(book);
      }
      return booksWithSaint;
    },
    bestTipikonPriorityHoliday() {
      return this.sortedHolidays?.[0];
    }
  },
  methods: { choiceHolidayColor }
};
</script>
