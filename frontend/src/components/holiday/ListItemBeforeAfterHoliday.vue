<template>
  <div v-if="holiday?.before_after_holidays.length">
    <v-list-item
      prepend-icon="mdi-calendar-range-outline"
    >
      Дни
      <v-chip
        v-if="hasPredprazdnstvo"
        :to="{ name: 'holiday', params: { holidaySlug: 'predprazdnstvo-' + holiday?.slug } }"
        variant="elevated"
        color="red-lighten-4"
        class="ma-1"
      >
        Предпразднства
      </v-chip>
      <span
        v-if="hasPredprazdnstvo && hasPoprazdnstvo"
      >
      и
      </span>
      <v-chip
        v-if="hasPoprazdnstvo"
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
  },
  computed: {
    hasPoprazdnstvo() {
      return !!this.holiday.before_after_holidays_attributes.find(attribute => attribute.popover.label.startsWith("Отдание"));
    },
    hasPredprazdnstvo() {
      return !!this.holiday.before_after_holidays_attributes.find(attribute => attribute.popover.label.startsWith("Предпразднство"));
    }
  }
};

</script>

