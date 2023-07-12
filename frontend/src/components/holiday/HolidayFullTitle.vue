<template>
  <ChipDay v-if="holiday.day" :day="holiday.day" />
  <ChipMovableDay else :movable_day="holiday.movable_day" />
  <ChipHolidayCategory :holiday_category="holiday.holiday_category" class="ml-1" />
  <span class="ml-1">{{ holiday.title }}</span>
  <ChipYear v-if="holiday.year" :year="holiday.year" class="ml-1" />
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";
import ChipDay from "@/components/day/ChipDay.vue";
import ChipHolidayCategory from "@/components/holiday/ChipHolidayCategory.vue";
import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";

export default {
  components: { ChipDay, ChipMovableDay, ChipYear, ChipHolidayCategory },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>



