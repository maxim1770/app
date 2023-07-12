<template>
  <v-row class="bg-red-lighten-3 border-b">
    <v-col
      cols="12"
      class="text-h6 text-red-accent-4 font-weight-bold"
    >
      Нд {{ week.sunday_num }}
      <template v-if="week.sunday_title">, {{ week.sunday_title }}</template>
      <!-- TODO запятая на сайте неправильно: 'text , '-->
    </v-col>
  </v-row>
  <v-row
    v-if="sundayMatins(week)"
    class="bg-red-lighten-3"
  >
    <v-col cols="2">
      <p v-if='sundayMatins(week).divine_service.title === "matins"'>
        На Утрене
      </p>
      <p v-else>
        На Вечерне
      </p>
    </v-col>
    <v-col offset="1" cols="4">
      <p class="text-red-accent-3">
        {{ sundayMatins(week).zachalos[0].title }}
      </p>
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="sundayMatins(week).zachalos[0]" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row class="bg-red-lighten-3 border-b-md">
    <v-col cols="2">
      На Литургии
    </v-col>
    <v-col
      v-for="zachalo in sundayLiturgyZachalos(week)"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row
    v-for="movable_day in week.movable_days.slice(1)"
    :key="movable_day.id"
    :class="{'rounded-shaped bg-red-lighten-3': movable_day.abbr === currentMovableDayAbbr}"
  >
    <v-col cols="2" class="text-capitalize">
      {{ movable_day.abbr_ru }}
    </v-col>
    <v-col
      v-for="zachalo in movable_day.movable_dates[0].zachalos.slice(0, 2)"
      v-if="movable_day.movable_dates[0]"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" />
    </v-col>
    <v-divider></v-divider>
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
  methods: {
    sundayMatins(week) {
      return week.movable_days[0].movable_dates.filter(movable_date => movable_date.divine_service.title !== "liturgy")[0];
    },
    sundayLiturgyZachalos(week) {
      return week.movable_days[0].movable_dates.filter(movable_date => movable_date.divine_service.title === "liturgy")[0].zachalos.slice(0, 2);
    }
  }
};

</script>



