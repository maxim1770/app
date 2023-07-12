<template>
  <v-list lines="one">
    <v-list-item
      v-if="holiday.before_after_holiday"
      :to="{ name: 'holiday', params: { holidaySlug: holiday.before_after_holiday.great_holiday.slug } }"
      prepend-icon="mdi-candelabra-fire"
      rounded="xl"
    >
      <HolidayFullTitle :holiday="holiday.before_after_holiday.great_holiday" />
    </v-list-item>
    <v-list-item
      prepend-icon="mdi-calendar-range"
    >
      ... {{ holiday.before_after_holiday.days.length }} дней
    </v-list-item>
  </v-list>
  <v-divider></v-divider>
</template>

<script>


import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";

export default {
  components: { HolidayFullTitle },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>



