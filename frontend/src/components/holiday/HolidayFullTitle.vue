<template>
  <ChipDay
    :day="holiday.day"
    class="ma-1"
  />
  <ChipMovableDay
    :movable_day="holiday.movable_day"
    class="ma-1"
  />
  <BadgeHolidayCategory
    :holiday_category="holiday.holiday_category"
    class="ma-1"
  />
  <span
    :class="choiceHolidayTextColor(holiday)"
    class="ma-1"
  >
    {{ holiday.title }}
  </span>
  <ChipYear
    :year="holiday.year"
    class="ma-1"
  />
  <ChipTipikon
    :tipikon="holiday.tipikon"
    class="ma-1"
  />
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";
import ChipDay from "@/components/day/ChipDay.vue";
import BadgeHolidayCategory from "@/components/holiday/holiday_category_title/BadgeHolidayCategory.vue";
import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";
import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import { choiceHolidayTextColor } from "@/utils/holidays";

export default {
  components: { ChipDay, ChipMovableDay, ChipYear, BadgeHolidayCategory, ChipTipikon },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  methods: { choiceHolidayTextColor }

};

</script>



