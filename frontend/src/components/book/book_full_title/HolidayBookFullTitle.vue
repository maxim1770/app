<template>
  <ChipDay v-if="book.holiday_book.holiday?.day" :day="book.holiday_book.holiday.day" />
  <v-chip v-if="book.type" class="ml-1">
    {{ book.type }}
    <template v-if="isGreatHoliday"> на</template>
    <template v-else-if="isDenPamjati && isBookTypePouchenie"> на Память</template>
    <template v-else-if="isBookTypeHasLetterO"> о</template>
  </v-chip>
  <v-chip v-else-if="isSaintLife && isDenPamjati" class="ml-1">Житие</v-chip>
  <v-chip v-if="book.holiday_book.holiday"
          :to="{ name: 'holiday', params: { holidaySlug: book.holiday_book.holiday.slug } }" class="ml-1">
    <template
      v-if="book.type && book.holiday_book.holiday.title_in_dative && !isBookTypePouchenie && !isGreatHoliday"
    >
      {{ book.holiday_book.holiday.title_in_dative }}
    </template>
    <template v-else>
      {{ book.holiday_book.holiday.title }}
    </template>
  </v-chip>
  <v-chip v-else :to="{ name: 'saint', params: { saintSlug: book.holiday_book.saint.slug } }" class="ml-1">
    <template
      v-if="book.type && book.holiday_book.saint.name_in_dative && !isBookTypePouchenie"
    >
      {{ book.holiday_book.saint.name_in_dative }}
    </template>
    <template v-else>
      {{ book.holiday_book.saint.name }}
    </template>
  </v-chip>
  <ChipYear v-if="book.holiday_book.holiday?.year" :year="book.holiday_book.holiday.year" class="ml-1" />
</template>

<!--<template v-if="book.holiday_book.book_util"> ({{ book.holiday_book.book_util }})</template>-->

<script>


import { isGreatHoliday } from "@/utils/holidays";
import ChipDay from "@/components/day/ChipDay.vue";
import ChipYear from "@/components/year/ChipYear.vue";

export default {
  components: { ChipDay, ChipYear },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    isGreatHoliday() {
      return isGreatHoliday(this.book.holiday_book.holiday?.holiday_category.title);
    },
    isDenPamjati() {
      return this.book.holiday_book.holiday?.holiday_category.title === "День памяти";
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



