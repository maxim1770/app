<template>
  <component
    :is="holidayFactory"
    :holiday="holiday"
  />
</template>

<script>

import BeforeAfterHoliday from "@/components/holiday/holiday/BeforeAfterHoliday.vue";
import SomeHoliday from "@/components/holiday/holiday/SomeHoliday.vue";


export default {
  components: {
    BeforeAfterHoliday, SomeHoliday
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  computed: {
    holidayFactory() {
      if (this.holiday?.before_after_holiday) {
        return BeforeAfterHoliday;
      } else {
        return SomeHoliday;
      }
    }
  }
};
</script>

