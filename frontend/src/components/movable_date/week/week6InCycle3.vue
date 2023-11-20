<template>
  <v-row :class="{'rounded-shaped bg-red-lighten-3': satWeek6?.abbr === currentMovableDayAbbr}">
    <v-col cols="2">
      {{ satWeek6?.abbr_ru }} {{ week6?.sunday_num }}, {{ satWeek6?.title }}
    </v-col>
    <v-col
      v-for="zachalo in satLiturgyWeek6"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" />
    </v-col>
  </v-row>
  <v-row :class="{'bg-red-lighten-3': sunWeek6?.abbr === currentMovableDayAbbr}">
    <v-col cols="2">
      {{ sunWeek6?.abbr_ru }} {{ week6?.sunday_num }}, {{ sunWeek6?.title }}
    </v-col>
    <v-col offset="1" cols="4">
      Евангелие на Утрене
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="sunMatinsWeek6" />
    </v-col>
  </v-row>
  <v-row :class="{'bg-red-lighten-3': sunWeek6?.abbr === currentMovableDayAbbr}">
    <v-col cols="2">
      На Литургии
    </v-col>
    <v-col
      v-for="zachalo in sunLiturgyWeek6"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="sunMatinsWeek6" />
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
    satWeek6() {
      return this.week.movable_days[5];
    },
    sunWeek6() {
      return this.week.movable_days[6];
    },
    satLiturgyWeek6() {
      return this.satWeek6.movable_dates.find(movable_date => movable_date.divine_service.title === "liturgy")?.zachalos.slice(0, 2);
    },
    sunMatinsWeek6() {
      return this.sunWeek6?.movable_dates.find(movable_date => movable_date.divine_service.title === "matins")?.zachalos[0];
    },
    sunLiturgyWeek6() {
      return this.sunWeek6?.movable_dates.find(movable_date => movable_date.divine_service.title === "liturgy")?.zachalos.slice(0, 2);
    }
  }
};

</script>



