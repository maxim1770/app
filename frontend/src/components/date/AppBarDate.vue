<template>
  <v-tooltip
    text="Новый день начинается с вечера"
    location="bottom"
  >
    <template v-slot:activator="{ props }">
      <v-btn
        v-if="date?.date_slug"
        v-bind="props"
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
              :content="isSunDate ? sunTitle : date.movable_day?.title || date?.movable_day.full_title"
              :color="movableDayBadgeColor"
            />
          </div>
        </div>
      </v-btn>
    </template>
  </v-tooltip>
</template>

<script>


import { choiceHolidayColor, prepareDateAllSortedHolidays } from "@/utils/holidays";
import { isSunDate } from "@/utils/date";

export default {
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  computed: {
    movableDayBadgeColor() {
      return this.isSunDate || this.date.movable_day?.title ? "red-accent-4" : "blue";
    },
    topTipikonHoliday() {
      return this.__allHolidays?.[0];
    },
    __allHolidays() {
      return prepareDateAllSortedHolidays(this.date);
    },
    sunTitle() {
      return this.date?.movable_day?.week?.sunday_title || this.date?.movable_day.full_title;
    },
    isSunDate() {
      return isSunDate(this.date);
    }
  },
  methods: { choiceHolidayColor }
};

</script>

