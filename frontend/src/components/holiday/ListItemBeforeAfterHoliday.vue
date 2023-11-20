<template>
  <div v-if="holiday?.before_after_holidays.length">
    <v-list-item
      prepend-icon="mdi-calendar-range-outline"
    >
      Дни
      <v-chip
        :to="{ name: 'holiday', params: { holidaySlug: 'predprazdnstvo-' + holiday?.slug } }"
        variant="elevated"
        color="red-lighten-4"
        class="ma-1"
      >
        Предпразднства
      </v-chip>
      и
      <v-chip
        :to="{ name: 'holiday', params: { holidaySlug: 'poprazdnstvo-' + holiday?.slug } }"
        variant="elevated"
        color="red-lighten-4"
        class="ma-1"
      >
        Попразднства
      </v-chip>
    </v-list-item>
    <BeforeAfterHolidayCalendar :attributes="holiday.before_after_holidays_attributes" />
  </div>
</template>

<script>


import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import BeforeAfterHolidayCalendar from "@/components/calendar/BeforeAfterHolidayCalendar.vue";

export default {
  components: { BeforeAfterHolidayCalendar, ChipTipikon },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }

};

</script>


