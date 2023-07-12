<template>
  <component
    :is="holidayCategoryFactory"
    :holiday="holiday"
  />
</template>

<script>

import HolidayCategoryGreatHoliday from "@/components/holiday/holiday_category/HolidayCategoryGreatHoliday.vue";
import HolidayCategorySaints from "@/components/holiday/holiday_category/HolidayCategorySaints.vue";
import HolidayCategorySaint from "@/components/holiday/holiday_category/HolidayCategorySaint.vue";
import { isGreatHoliday } from "@/utils/holidays";


export default {
  components: {
    HolidayCategoryGreatHoliday, HolidayCategorySaints, HolidayCategorySaint
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  computed: {
    holidayCategoryFactory() {
      if (this.isGreatHoliday) {
        return HolidayCategoryGreatHoliday;
      } else if (this.holiday.saints?.length > 1) {
        return HolidayCategorySaints;
      } else {
        return HolidayCategorySaint;
      }
    },
    isGreatHoliday() {
      return isGreatHoliday(this.holiday.holiday_category?.title);
    }
  }
};
</script>

