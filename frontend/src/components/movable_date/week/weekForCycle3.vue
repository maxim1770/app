<template>
  <v-row
    v-for="movable_day in [sun, sat]"
    :key="movable_day.id"
    :class="{'rounded-shaped bg-red-lighten-3': movable_day.abbr === currentMovableDayAbbr}"
  >
    <v-col cols="2" class="text-capitalize">
      {{ movable_day.abbr_ru.replace("вс", "Нд") }} {{ week.sunday_num + addOneToSat(movable_day) }}
    </v-col>
    <v-col
      v-for="zachalo in chooseEvangelAndApostleZachalos(movable_day.movable_dates[0].zachalos)"
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
    sun() {
      return this.week.movable_days.find(movable_date => movable_date.abbr === "sun");
    },
    sat() {
      return this.week.movable_days.find(movable_date => movable_date.abbr === "sat");
    }
  },
  methods: {
    addOneToSat(movable_day) {
      return movable_day.abbr === this.sat?.abbr ? 1 : 0;
    },
    chooseEvangelAndApostleZachalos(zachalos) {
      return chooseEvangelAndApostleZachalos(zachalos);
    }
  }
};

</script>
