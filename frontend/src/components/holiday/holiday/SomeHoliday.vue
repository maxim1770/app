<template>
  <v-card>
    <v-card-item>
      <v-list>
        <ListItemHolidayCategory :holiday="holiday" />
        <ListItemTipikon :tipikon="holiday?.tipikon" />
        <ListItemYear :year="holiday?.year" />
        <ListItemDay :day="holiday?.day" />
        <ListItemMovableDay :movable_day="holiday?.movable_day" />
        <ListItemBeforeAfterHoliday :holiday="holiday" />
      </v-list>
    </v-card-item>
  </v-card>
  <HolidayCategoryFactory :holiday="holiday" />
</template>

<script>


import HolidayCategoryFactory from "@/components/holiday/holiday_category/HolidayCategoryFactory.vue";
import ListItemDay from "@/components/day/ListItemDay.vue";
import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemMovableDay from "@/components/movable_day/ListItemMovableDay.vue";
import ListItemTipikon from "@/components/holiday/tipikon/ListItemTipikon.vue";
import BeforeAfterHolidayCalendar from "@/components/calendar/BeforeAfterHolidayCalendar.vue";
import ListItemBeforeAfterHoliday from "@/components/holiday/ListItemBeforeAfterHoliday.vue";
import ListItemHolidayCategory from "@/components/holiday/holiday_category_title/ListItemHolidayCategory.vue";

export default {
  components: {
    ListItemHolidayCategory,
    BeforeAfterHolidayCalendar,
    ListItemTipikon,
    HolidayCategoryFactory,
    ListItemDay,
    ListItemMovableDay,
    ListItemYear,
    ListItemBeforeAfterHoliday
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>



