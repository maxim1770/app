<template>
  <MolitvaBookForHoliday :molitva_books_by_manuscript="molitva_books_by_manuscript" :holiday="holiday" />
  <HolidayBookForHoliday :holidayBooksWithoutUpominanies="holidayBooksWithoutUpominanies" :holiday="holiday" :saint="saint"/>
  <UpominanieBookForHoliday :upominanieBooks="upominanieBooks" :holiday="holiday" :saint="saint"/>
</template>


<script>

import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import MolitvaBookForHoliday from "@/components/book/book_for_holiday/MolitvaBookForHoliday.vue";
import HolidayBookForHoliday from "@/components/book/book_for_holiday/HolidayBookForHoliday.vue";
import UpominanieBookForHoliday from "@/components/book/book_for_holiday/UpominanieBookForHoliday.vue";

export default {
  components: { UpominanieBookForHoliday, HolidayBookForHoliday, MolitvaBookForHoliday, ListItemManuscript },
  props: {
    molitva_books_by_manuscript: {
      type: Object,
      required: true
    },
    holiday_books: {
      type: Array,
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
    holidayBooksWithoutUpominanies() {
      const holidayBooksWithoutUpominanies = [];
      this.holiday_books?.forEach((holiday_book) => {
        if (holiday_book?.book_util !== "Упоминание") {
          holidayBooksWithoutUpominanies.push(holiday_book);
        }
      });
      return holidayBooksWithoutUpominanies;
    },
    upominanieBooks() {
      const upominanieBooks = [];
      this.holiday_books?.forEach((holiday_book) => {
        if (holiday_book?.book_util === "Упоминание") {
          upominanieBooks.push(holiday_book);
        }
      });
      return upominanieBooks;
    }
  }
};
</script>