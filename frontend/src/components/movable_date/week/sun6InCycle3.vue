<template>
  <v-row :class="{'bg-red-lighten-3': sunWeek6?.abbr === currentMovableDayAbbr}">
    <v-col cols="2">
      Нд 6, {{ sunWeek6?.title }}
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
      :key="zachalo?.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" />
    </v-col>
  </v-row>
</template>

<script>

import ChipZachalo from "@/components/book/ChipZachalo.vue";
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
    sunMatinsWeek6() {
      return this.sunWeek6?.movable_dates.find(movable_date => movable_date.divine_service.title === "matins")?.zachalos[0];
    },
    sunLiturgyWeek6() {
      return chooseEvangelAndApostleZachalos(this.sunWeek6?.movable_dates.find(movable_date => movable_date.divine_service.title === "liturgy")?.zachalos);
    }
  }
};

</script>
