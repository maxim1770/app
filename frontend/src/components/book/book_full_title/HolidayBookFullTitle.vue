<template>
  <ChipDay
    :day="Holiday?.day"
    class="ma-1"
  />
  <ChipMovableDay
    :movable_day="Holiday?.movable_day"
    class="ma-1"
  />
  <v-chip
    v-if="book.type || isSaintLife && (isDenPamjati || Saint) || isPaterik && Saint || holidayBook.book_util === 'Упоминание' || holidayBook.book_util === 'Чудо' || book.title === 'Пролог'"
    color="pink-darken-1"
    class="ma-1"
  >
    <template v-if="book.type">
      {{ book.type }}
      <template v-if="isGreatHoliday"> на</template>
      <template v-else-if="isDenPamjati && isBookTypePouchenie"> на Память</template>
      <template v-else-if="isBookTypeHasLetterO"> о</template>
    </template>
    <template v-else-if="isPaterik && Saint">
      О
    </template>
    <template v-else-if="isSaintLife && (isDenPamjati || Saint)">
      Житие
    </template>
    <template v-else-if="holidayBook.book_util === 'Упоминание'">
      Упоминание
    </template>
    <template v-else-if="holidayBook.book_util === 'Чудо'">
      Чудо
    </template>
    <template v-else-if="book.title === 'Пролог'">
      Пролог
    </template>
  </v-chip>
  <router-link
    v-if="Holiday"
    :to="{ name: 'holiday', params: { holidaySlug: Holiday.slug } }"
    :class="choiceHolidayTextColor(Holiday)"
    class="text-decoration-none ma-1"
  >
    {{ holidayTitle }}
  </router-link>
  <router-link
    v-else-if="Saint"
    :to="{ name: 'saint', params: { saintSlug: Saint.slug } }"
    :class="choiceHolidayTextColor(Holiday)"
    class="text-decoration-none ma-1"
  >
    {{ saintTitle }}
  </router-link>
  <ChipYear
    :year="Holiday?.year"
    class="ma-1"
  />
  <ChipTipikon
    :tipikon="Holiday?.tipikon"
    class="ma-1"
  />
  <BadgeFaceSanctity
    :face_sanctity="Saint?.face_sanctity"
    class="ma-1"
  />
  <BadgeDignity
    :dignity="Saint?.dignity"
    class="ma-1"
  />
  <BookAuthor :saint="book.author" />
</template>


<script>


import { choiceHolidayTextColor, isGreatHoliday } from "@/utils/holidays";
import ChipDay from "@/components/day/ChipDay.vue";
import ChipYear from "@/components/year/ChipYear.vue";
import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import BadgeDignity from "@/components/saint/dignity/BadgeDignity.vue";
import BadgeFaceSanctity from "@/components/saint/face_sanctity/BadgeFaceSanctity.vue";
import BookAuthor from "@/components/book/book_full_title/__BookAuthor.vue";
import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";

export default {
  components: { ChipMovableDay, BookAuthor, BadgeFaceSanctity, BadgeDignity, ChipTipikon, ChipDay, ChipYear },
  props: {
    book: {
      type: Object,
      required: true
    },
    holiday_book: {
      type: Object,
      required: false,
      default: null
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
    holidayBook() {
      return this.holiday_book ? this.holiday_book : this.book.holiday_book;
    },
    Holiday() {
      return this.holiday ? this.holiday : this.holidayBook?.holiday;
    },
    Saint() {
      if (!this.Holiday) {
        return this.saint ? this.saint : this.holidayBook?.saint;
      } else {
        return null;
      }
    },
    holidayTitle() {
      return this.book.type && this.Holiday.title_in_dative && !this.isBookTypePouchenie && !this.isGreatHoliday ? this.Holiday.title_in_dative : this.Holiday.title;
    },
    saintTitle() {
      if (this.book.type && this.Saint.name_in_dative && !this.isBookTypePouchenie) {
        return this.Saint.name_in_dative;
      } else if (this.Saint?.name_in_genitive) {
        return this.Saint.name_in_genitive;
      } else {
        return this.Saint.name;
      }
    },
    isGreatHoliday() {
      return isGreatHoliday(this.Holiday?.holiday_category.title);
    },
    isDenPamjati() {
      return this.Holiday?.holiday_category.title === "День памяти";
    },
    isBookTypeHasLetterO() {
      return this.BOOK_TYPES_HAS_LETTER_O.includes(this.book.type);
    },
    isBookTypePouchenie() {
      return this.book.type === "Поучение";
    },
    isSaintLife() {
      return this.BOOK_TITLES_HAS_SAINT_LIFE.includes(this.book.title);
    },
    isPaterik() {
      return this.book.title === "Патерик";
    }
  },
  created() {
    this.BOOK_TYPES_HAS_LETTER_O = ["Слово", "Притча", "Повесть", "Беседа"];
    this.BOOK_TITLES_HAS_SAINT_LIFE = ["Жития Святых", "Сборник Слов и Житий", "Службы и Жития Святых", "Патерик"];
  },
  methods: { choiceHolidayTextColor }
};

</script>



