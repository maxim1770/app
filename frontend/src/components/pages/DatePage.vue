<template>
  <div>
    <CarouselMain :imgs_data="allIcons" :has_cover="false" />
    <DateHead :date="date" />
    <!--    <AdminTableDateHolidays :date="date" />-->
    <ListHolidays :holidays="allHolidays" />
    <ZachaloBookForDate :movable_day="date.movable_day" />
    <MovableDateBookForDate :movable_date_books="movableDateBooks" />
    <BooksForHoliday
      :molitva_books_by_manuscript="date.day?.molitva_books_by_manuscript"
      :holiday_books="allHolidaysBooks"
    />
    <CardRandomBook />
  </div>
</template>


<script>

import AdminTableDateHolidays from "@/components/date/AdminTableDateHolidays.vue";
import ListHolidays from "@/components/holiday/ListHolidays.vue";
import DateHead from "@/components/date/DateHead.vue";
import MovableDateBookForDate from "@/components/book/book_for_date/MovableDateBookForDate.vue";
import ZachaloBookForDate from "@/components/book/book_for_date/ZachaloBookForDate.vue";
import BooksForHoliday from "@/components/book/book_for_holiday/BooksForHoliday.vue";
import CarouselMain from "@/components/gallery/CarouselMain.vue";
import { prepareAllHolidaysBooks, prepareAllIcons, prepareDateAllSortedHolidays } from "@/utils/holidays";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";


export default {
  components: {
    CardRandomBook,
    CarouselMain,
    BooksForHoliday,
    ZachaloBookForDate,
    MovableDateBookForDate,
    DateHead,
    ListHolidays,
    AdminTableDateHolidays
  },
  props: {
    date: {
      type: Object,
      required: true
    }
  },

  computed: {
    movableDateBooks() {
      let movableDateBooks = [];
      for (let movable_date_book of this.date.movable_day?.movable_date_books) {
        movable_date_book.movable_day = this.date.movable_day;
        movableDateBooks.push(movable_date_book);
      }
      return movableDateBooks;
    },
    allHolidays() {
      return prepareDateAllSortedHolidays(this.date);
    },
    allHolidaysBooks() {
      return prepareAllHolidaysBooks(this.allHolidays);
    },
    allIcons() {
      return prepareAllIcons(this.allHolidays);
    }

  }
};
</script>
