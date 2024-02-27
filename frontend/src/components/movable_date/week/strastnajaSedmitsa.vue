<template>
  <template
    v-for="movable_day in [monStrastnajaSedmitsa, tueStrastnajaSedmitsa, wedStrastnajaSedmitsa, thuStrastnajaSedmitsa]"
    :key="movable_day.id"
  >
    <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': movable_day.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': movable_day.abbr !== currentMovableDayAbbr
    }">
      <v-col class="red-accent-4 text-red-accent-3">
        {{ movable_day.title }}
      </v-col>
    </v-row>
    <v-row>
      <v-col offset="1" cols="6">
        На Литургии
      </v-col>
      <v-col cols="5">
        <ChipZachalo :zachalo="dayLiturgyStrastnajaSedmitsa(movable_day)" color="red-accent-3" />
      </v-col>
    </v-row>
  </template>
  <v-row
    no-gutters
    class="mt-2"
  >
    <v-col offset="1" cols="6">
      На умовение ногам
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="thuUmyveniyeStrastnajaSedmitsa?.[0]" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row
    no-gutters
    class="mt-1"
  >
    <v-col offset="1" cols="6">
      По умовению
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="thuUmyveniyeStrastnajaSedmitsa?.[1]" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row
    no-gutters
    class="mt-2"
  >
    <v-col offset="1" cols="6">
      Апостол на Вечерне
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="thuVespersStrastnajaSedmitsa" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col class="red-accent-4 text-red-accent-4 bg-red-lighten-3 mb-3">
      Евангелия 12 Святых Страстей Господа Бога и Спаса нашего Исуса Христа
    </v-col>
  </v-row>
  <v-row
    v-for="zachalo in [
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 46 && zachalo.bible_book.abbr === 'jn'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 58 && zachalo.bible_book.abbr === 'jn'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 109 && zachalo.bible_book.abbr === 'mt'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 59 && zachalo.bible_book.abbr === 'jn'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 111 && zachalo.bible_book.abbr === 'mt'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 67 && zachalo.bible_book.abbr === 'mk'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 113 && zachalo.bible_book.abbr === 'mt'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 111 && zachalo.bible_book.abbr === 'lk'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 61 && zachalo.bible_book.abbr === 'jn'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 69 && zachalo.bible_book.abbr === 'mk'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 62 && zachalo.bible_book.abbr === 'jn'),
      friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 114 && zachalo.bible_book.abbr === 'mt'),
    ]"
    :key="zachalo?.id"
    no-gutters
    class="mt-3"
  >
    <v-col>
      <ChipZachalo
        :zachalo="zachalo"
        color="red-accent-3"
        :style="{ 'width': mdAndUp ? '140px' : '90px' }"
      />
    </v-col>
  </v-row>
  <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': friStrastnajaSedmitsa.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': friStrastnajaSedmitsa.abbr !== currentMovableDayAbbr
    }"
  >
    <v-col class="red-accent-4 text-red-accent-3">
      Последование часов Святой и Великой Пятницы
    </v-col>
  </v-row>
  <v-row
    v-for="i in 4"
  >
    <v-col cols="2">
      На Часе
      <template v-if="(i - 1) * 3 === 0">1</template>
      <template v-else>{{ (i - 1) * 3 }}</template>
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="friHoursStrastnajaSedmitsa[i - 1]?.[0]" color="red-accent-3" />
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="friHoursStrastnajaSedmitsa[i - 1]?.[1]" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      На Вечерне
    </v-col>
    <v-col
      v-for="zachalo in friVespersStrastnajaSedmitsa"
      :key="zachalo?.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': satStrastnajaSedmitsa.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': satStrastnajaSedmitsa.abbr !== currentMovableDayAbbr
    }"
  >
    <v-col class="red-accent-4 text-red-accent-3">
      {{ satStrastnajaSedmitsa.title }}
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      На Утрене
    </v-col>
    <v-col
      v-for="zachalo in satMatinsStrastnajaSedmitsa"
      :key="zachalo?.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      Вечер на Литургии (или Вечерня) (не знаю)
    </v-col>
    <v-col
      v-for="zachalo in satLiturgyStrastnajaSedmitsa"
      :key="zachalo?.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="red-accent-3" />
    </v-col>
  </v-row>
</template>

<script>

import ChipZachalo from "@/components/book/ChipZachalo.vue";
import { useDisplay } from "vuetify";
import { chooseEvangelAndApostleZachalos } from "@/utils/zachalos";

export default {
  components: { ChipZachalo },
  props: {
    week: {
      type: Object,
      required: true
    },
    currentMovableDayAbbr: {
      type: String,
      required: false,
      default: null
    }
  },
  computed: {
    sunWeek6() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "sun");
    },
    monStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "mon");
    },
    tueStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "tue");
    },
    wedStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "wed");
    },
    thuStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "thu");
    },
    friStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "fri");
    },
    satStrastnajaSedmitsa() {
      return this.week?.movable_days.find(movable_date => movable_date.abbr === "sat");
    },
    thuUmyveniyeStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service === null)?.zachalos;
    },
    thuVespersStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service?.title === "vespers")?.zachalos[0];
    },
    friCommonStrastnajaSedmitsa() {
      return this.friStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service === null)?.zachalos;
    },
    friHoursStrastnajaSedmitsa() {
      return [
        [
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 111 && zachalo.bible_book.abbr === "mt"),
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 215 && zachalo.bible_book.abbr === "gal")
        ],
        [
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 66 && zachalo.bible_book.abbr === "mk"),
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 88 && zachalo.bible_book.abbr === "rom")
        ],
        [
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 110 && zachalo.bible_book.abbr === "lk"),
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 306 && zachalo.bible_book.abbr === "hebr")
        ],
        [
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 59 && zachalo.bible_book.abbr === "jn"),
          this.friCommonStrastnajaSedmitsa.find(zachalo => zachalo.num === 324 && zachalo.bible_book.abbr === "hebr")
        ]
      ];
    },
    friVespersStrastnajaSedmitsa() {
      return chooseEvangelAndApostleZachalos(this.friStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service?.title === "vespers")?.zachalos);
    },
    satMatinsStrastnajaSedmitsa() {
      return chooseEvangelAndApostleZachalos(this.satStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service.title === "matins")?.zachalos);
    },
    satLiturgyStrastnajaSedmitsa() {
      return chooseEvangelAndApostleZachalos(this.satStrastnajaSedmitsa.movable_dates.find(movable_date => movable_date.divine_service.title === "liturgy")?.zachalos);
    }
  },
  setup() {
    const mdAndUp = useDisplay();
    return mdAndUp;
  },
  methods: {
    dayLiturgyStrastnajaSedmitsa(movable_day) {
      return movable_day.movable_dates.find(movable_date => movable_date.divine_service?.title === "liturgy")?.zachalos[0];
    }
  }
};

</script>
