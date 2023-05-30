<template>
  <v-chip :to="{ name: 'date', params: { date: book.holiday_book.holiday.day.month_day } }">
    {{ book.holiday_book.holiday.day.title }}
  </v-chip>
  <v-chip v-if="book.type">
    {{ book.type }}
    <template v-if="isGreatHoliday"> на</template>
    <template v-else-if="isDenPamjati && isBookTypePouchenie"> на Память</template>
    <template v-else-if="isBookTypeHasLetterO"> о</template>
  </v-chip>
  <v-chip v-else-if="isSaintLife && isDenPamjati">Житие</v-chip>
  <v-chip :to="{ name: 'holiday', params: { holidaySlug: book.holiday_book.holiday.slug } }">
    <template
      v-if="book.type && book.holiday_book.holiday.title_in_dative && !isBookTypePouchenie && !isGreatHoliday">
      {{ book.holiday_book.holiday.title_in_dative }}
    </template>
    <template v-else>
      {{ book.holiday_book.holiday.title }}
    </template>
  </v-chip>
</template>

<!--<template v-if="book.holiday_book.book_util"> ({{ book.holiday_book.book_util }})</template>-->

<script>


import { isGreatHoliday } from "@/utils/holidays";

export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    isGreatHoliday() {
      return isGreatHoliday(this.book.holiday_book.holiday.holiday_category?.title);
    },
    isDenPamjati() {
      return this.book.holiday_book.holiday.holiday_category.title === "День памяти";
    },
    isBookTypeHasLetterO() {
      return this.BOOK_TYPES_HAS_LETTER_O.includes(this.book.type);
    },
    isBookTypePouchenie() {
      return this.book.type === "Поучение";
    },
    isSaintLife() {
      return this.BOOK_TITLES_HAS_SAINT_LIFE.includes(this.book.title);
    }
  },
  created() {
    this.BOOK_TYPES_HAS_LETTER_O = ["Слово", "Притча", "Повесть", "Беседа"];
    this.BOOK_TITLES_HAS_SAINT_LIFE = ["Жития Святых", "Сборник Слов и Житий"];
  }
};

</script>



