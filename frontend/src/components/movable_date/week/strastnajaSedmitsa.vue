<template>
  <template
    v-for="movable_day in week.movable_days.slice(0, 4)"
    :key="movable_day.id"
  >
    <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': movable_day.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': movable_day.abbr !== currentMovableDayAbbr
    }">
      <v-col cols="12" class="text-red-accent-4">
        {{ movable_day.title }}
      </v-col>
    </v-row>
    <v-row>
      <v-col offset="1" cols="6">
        На Литургии
      </v-col>
      <v-col cols="5">
        <ChipZachalo :zachalo="dayLiturgyStrastnajaSedmitsa(movable_day)" color="text-red-accent-3" />
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
      <ChipZachalo :zachalo="thuUmyveniyeStrastnajaSedmitsa[0]" color="text-red-accent-3" />
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
      <ChipZachalo :zachalo="thuUmyveniyeStrastnajaSedmitsa[1]" color="text-red-accent-3" />
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
      <ChipZachalo :zachalo="thuVespersStrastnajaSedmitsa" color="text-red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="12" class="text-red-accent-4 bg-red-lighten-3 mb-3">
      Евангелия 12 Святых Страстей Господа Бога и Спаса нашего Исуса Христа
    </v-col>
  </v-row>
  <v-row
    v-for="zachalo in friCommonStrastnajaSedmitsa.slice(0, 12)"
    :key="zachalo.id"
    no-gutters
    class="mt-3"
  >
    <v-col cols="12">
      <ChipZachalo :zachalo="zachalo" style="width: 100px;" color="text-red-accent-3" />
    </v-col>
  </v-row>
  <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': friStrastnajaSedmitsa.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': friStrastnajaSedmitsa.abbr !== currentMovableDayAbbr
    }"
  >
    <v-col cols="12" class="text-red-accent-4">
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
      <ChipZachalo :zachalo="friCommonStrastnajaSedmitsa[11 + i]" color="text-red-accent-3" />
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="friCommonStrastnajaSedmitsa[15 + i]" color="text-red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      На Вечерне
    </v-col>
    <v-col
      v-for="zachalo in friVespersStrastnajaSedmitsa"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="text-red-accent-3" />
    </v-col>
  </v-row>
  <v-row :class="{
      'bg-red-lighten-2 rounded-shaped': satStrastnajaSedmitsa.abbr === currentMovableDayAbbr,
      'bg-red-lighten-3': satStrastnajaSedmitsa.abbr !== currentMovableDayAbbr
    }"
  >
    <v-col cols="12" class="text-red-accent-4">
      {{ satStrastnajaSedmitsa.title }}
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      На Утрене
    </v-col>
    <v-col
      v-for="zachalo in satMatinsStrastnajaSedmitsa"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="text-red-accent-3" />
    </v-col>
  </v-row>
  <v-row>
    <v-col cols="2">
      Вечер на Литургии (или Вечерня) (не знаю)
    </v-col>
    <v-col
      v-for="zachalo in satLiturgyStrastnajaSedmitsa"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="text-red-accent-3" />
    </v-col>
  </v-row>
</template>

<script>

import ChipZachalo from "@/components/book/ChipZachalo.vue";

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
    thuStrastnajaSedmitsa() {
      return this.week.movable_days[3];
    },
    friStrastnajaSedmitsa() {
      return this.week.movable_days[4];
    },
    satStrastnajaSedmitsa() {
      return this.week.movable_days[5];
    },
    thuUmyveniyeStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service === null)[0].zachalos;
    },
    thuVespersStrastnajaSedmitsa() {
      return this.thuStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service?.title === "vespers")[0].zachalos[0];
    },
    friCommonStrastnajaSedmitsa() {
      return this.friStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service === null)[0].zachalos;
    },
    friVespersStrastnajaSedmitsa() {
      return this.friStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service?.title === "vespers")[0].zachalos.slice(0, 2);
    },
    satMatinsStrastnajaSedmitsa() {
      return this.satStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service.title === "matins")[0].zachalos.slice(0, 2);
    },
    satLiturgyStrastnajaSedmitsa() {
      return this.satStrastnajaSedmitsa.movable_dates.filter(movable_date => movable_date.divine_service.title === "liturgy")[0].zachalos.slice(0, 2);
    }
  },
  methods: {
    dayLiturgyStrastnajaSedmitsa(movable_day) {
      return movable_day.movable_dates.filter(movable_date => movable_date.divine_service?.title === "liturgy")[0].zachalos[0];
    }
  }
};

</script>



