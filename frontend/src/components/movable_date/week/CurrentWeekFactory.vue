<template>
  <component
    :is="currentWeek"
    :week="week"
    :currentMovableDayAbbr="currentMovableDayAbbr"
  />
</template>

<script>


import weekForCycle3 from "@/components/movable_date/week/weekForCycle3.vue";
import weekForCycle1And2 from "@/components/movable_date/week/weekForCycle1And2.vue";
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";
import week1InCycle3 from "@/components/movable_date/week/week1InCycle3.vue";
import sun6InCycle3 from "@/components/movable_date/week/sun6InCycle3.vue";

export default {
  props: {
    week: {
      type: Object,
      required: true
    },
    currentMovableDayAbbr: {
      type: String,
      required: false,
      default: null
    }
  },
  computed: {
    currentWeek() {
      if (this.week?.cycle.num !== 3) {
        return weekForCycle1And2;
      } else if (!this.week?.num && this.currentMovableDayAbbr === "sun") {
        return sun6InCycle3;
      } else if (!this.week?.num) {
        return strastnajaSedmitsa;
      } else if (this.week?.num === 1) {
        return week1InCycle3;
      } else {
        return weekForCycle3;
      }
    }
  }
};
</script>
