<template>
  <v-row
    v-for="movable_day in week.movable_days.slice(5)"
    :key="movable_day.id"
    :class="{'rounded-shaped bg-red-lighten-3': movable_day.abbr === currentMovableDayAbbr}"
  >
    <v-col cols="2">
      {{ movable_day.abbr_ru.replace("вс", "нд") }} {{ week.sunday_num }}
    </v-col>
    <v-col
      v-for="zachalo in movable_day.movable_dates[0].zachalos.slice(0, 2)"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" />
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
  }
};

</script>



