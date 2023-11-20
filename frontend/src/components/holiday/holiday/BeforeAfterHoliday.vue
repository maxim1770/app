<template>
  <v-card>
    <v-card-item>
      <v-list>
        <v-list-item
          v-if="holiday.before_after_holiday"
          :to="{ name: 'holiday', params: { holidaySlug: holiday.before_after_holiday.great_holiday.slug } }"
        >
          <template v-slot:prepend>
            <v-icon
              icon="mdi-candelabra-fire"
              :color="choiceHolidayColor(holiday.before_after_holiday.great_holiday)"
            />
          </template>
          <HolidayFullTitle :holiday="holiday.before_after_holiday.great_holiday" />
        </v-list-item>
        <ListItemTipikon :tipikon="holiday?.tipikon" />
        <v-list-item
          prepend-icon="mdi-calendar-range"
        >
          Дни
        </v-list-item>
        <BeforeAfterHolidayCalendar :attributes="holiday.before_after_holiday.attributes" />
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";
import { offsetYear2year } from "@/utils/date";
import BeforeAfterHolidayCalendar from "@/components/calendar/BeforeAfterHolidayCalendar.vue";
import ListItemTipikon from "@/components/holiday/tipikon/ListItemTipikon.vue";
import { choiceHolidayColor } from "@/utils/holidays";

export default {
  components: { ListItemTipikon, HolidayFullTitle, BeforeAfterHolidayCalendar },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  computed: {},
  methods: {
    choiceHolidayColor,
    toSelectedDate(CalendarDay) {
      const year = offsetYear2year(CalendarDay.year, CalendarDay.month);
      this.$router.push({ name: "date", params: { dateSlug: CalendarDay.id.replace(CalendarDay.year, year) } });
    }

  }
};

</script>



