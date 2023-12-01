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
    :color="bookTypeColor"
    class="ma-1"
  >
    {{ book.type }}
  </v-chip>
  <router-link
    :to="{ name: 'holiday', params: { holidaySlug: Holiday.slug } }"
    :class="choiceHolidayTextColor(Holiday)"
    class="text-decoration-none ma-1"
  >
    {{ holidayTitle }}
  </router-link>
  <v-chip
    v-if="molitvaBook.glas_num"
    color="blue-lighten-2"
    class="ma-1"
  >
    Глас
    <BadgeNum
      :num="molitvaBook.glas_num"
      color="blue"
      class="ml-1"
    />
  </v-chip>
  <ChipTipikon
    :tipikon="Holiday?.tipikon"
    class="ma-1"
  />
  <ChipYear
    :year="Holiday?.year"
    class="ma-1"
  />
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";
import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import ChipDay from "@/components/day/ChipDay.vue";
import ChipYear from "@/components/year/ChipYear.vue";
import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";
import { choiceHolidayTextColor } from "@/utils/holidays";

export default {
  components: { ChipMovableDay, ChipYear, ChipDay, ChipTipikon, BadgeNum },
  props: {
    book: {
      type: Object,
      required: true
    },
    molitva_book: {
      type: Object,
      required: false,
      default: null
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    }
  },
  computed: {
    molitvaBook() {
      return this.molitva_book || this.book.molitva_book;
    },
    Holiday() {
      return this.holiday || this.molitvaBook.holiday;
    },
    holidayTitle() {
      return this.Holiday.title_in_dative || this.Holiday.title;
    },
    bookTypeColor() {
      return this.book.type === "Тропарь" ? "amber-darken-1" : "teal-lighten-1";
    }
  },
  methods: { choiceHolidayTextColor }
};

</script>

