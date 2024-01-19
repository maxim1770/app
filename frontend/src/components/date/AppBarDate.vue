<template>
  <v-btn
    v-if="date?.date_slug"
    @click="$router.push({ name: 'date', params: { dateSlug: date.date_slug } })"
    :color="choiceHolidayColor(topTipikonHoliday) || movableDayBadgeColor"
    rounded="xl"
    class="d-flex"
  >
    <template v-slot:prepend>
      <v-icon
        icon="mdi-calendar-today-outline"
        size="x-large"
      />
    </template>
    <div>
      <strong>{{ date?.day.title }}</strong>
      <div
        class="text-caption mt-1"
      >
        <v-badge
          :content="date?.movable_day.full_title"
          :color="movableDayBadgeColor"
        />
      </div>
    </div>
  </v-btn>
</template>

<script>


import { choiceHolidayColor, prepareDateAllSortedHolidays } from "@/utils/holidays";

export default {
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  computed: {
    movableDayBadgeColor() {
      return this.date?.movable_day.abbr === "sun" ? "red-accent-4" : "blue";
    },
    topTipikonHoliday() {
      return this.__allHolidays?.[0];
    },
    __allHolidays() {
      return prepareDateAllSortedHolidays(this.date);
    }
  },
  methods: { choiceHolidayColor }
};

</script>



