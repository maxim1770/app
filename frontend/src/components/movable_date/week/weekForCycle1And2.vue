<template>
  <v-row class="bg-red-lighten-3 border-b">
    <v-col>
      <MainSmallTitle
        :title="`Нд ${week?.sunday_num}${week?.sunday_title ? ', ' + week?.sunday_title : ''}`"
        :hasMargin="false"
        textColor="red-accent-4"
      />
    </v-col>
  </v-row>
  <v-row
    v-if="sundayMatins"
    class="bg-red-lighten-3"
  >
    <v-col cols="2" class="text-red-accent-3">
      <p v-if='sundayMatins.divine_service.title === "matins"'>
        На Утрене
      </p>
      <p v-else>
        На Вечерне
      </p>
    </v-col>
    <v-col offset="1" cols="4">
      <p class="text-red-accent-3">
        {{ sundayMatins.zachalos[0].title }}
      </p>
    </v-col>
    <v-col cols="5">
      <ChipZachalo :zachalo="sundayMatins.zachalos[0]" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row class="bg-red-lighten-3">
    <v-col cols="2" class="text-red-accent-3">
      На Литургии
    </v-col>
    <v-col
      v-for="zachalo in sundayLiturgyZachalos"
      :key="zachalo?.id"
      cols="5"
    >
      <ChipZachalo :zachalo="zachalo" color="red-accent-3" />
    </v-col>
  </v-row>
  <v-row
    v-for="movable_day in sortedMovableDays.slice(1)"
    :key="movable_day.id"
    :class="{'rounded-shaped bg-red-lighten-3': movable_day.abbr === currentMovableDayAbbr || movable_day?.title}"
  >
    <v-col
      cols="2"
      class="text-capitalize"
      :class="{'text-red-accent-3': movable_day?.title}"
    >
      {{ movable_day?.title || movable_day.abbr_ru }}
      <v-tooltip
        activator="parent"
      >
        {{ week.title }}
      </v-tooltip>
    </v-col>
    <v-col
      v-for="zachalo in chooseEvangelAndApostleZachalos(movable_day.movable_dates[0]?.zachalos)"
      v-if="movable_day.movable_dates[0]"
      :key="zachalo.id"
      cols="5"
    >
      <ChipZachalo
        :zachalo="zachalo"
        :color="movable_day?.title ? 'red-accent-3' : 'success'"
      />
    </v-col>
  </v-row>
</template>

<script>

import ChipZachalo from "@/components/book/ChipZachalo.vue";
import { chooseEvangelAndApostleZachalos } from "@/utils/zachalos";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle, ChipZachalo },
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
    sortedMovableDays() {
      return Object.values(this.week?.movable_days).sort((movable_day_1, movable_day_2) => movable_day_1.id > movable_day_2.id ? 1 : -1);
    },
    sundayMatins() {
      return this.sortedMovableDays[0]?.movable_dates.find(movable_date => movable_date.divine_service.title !== "liturgy");
    },
    sundayLiturgyZachalos() {
      return chooseEvangelAndApostleZachalos(this.sortedMovableDays[0]?.movable_dates.find(movable_date => movable_date.divine_service.title === "liturgy")?.zachalos);
    }
  },
  methods: {
    chooseEvangelAndApostleZachalos(zachalos) {
      return chooseEvangelAndApostleZachalos(zachalos);
    }
  }
};

</script>
