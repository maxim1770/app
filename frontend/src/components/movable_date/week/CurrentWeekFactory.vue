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
import week6InCycle3 from "@/components/movable_date/week/week6InCycle3.vue";
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";

export default {
  components: {
    weekForCycle3, weekForCycle1And2, week6InCycle3, strastnajaSedmitsa
  },
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
      if (this.week.cycle.num !== 3) {
        return weekForCycle1And2;
      } else if (!this.week.num) {
        return strastnajaSedmitsa;
      } else if (this.week.num === 6) {
        return week6InCycle3;
      } else {
        return weekForCycle3;
      }
    }
  }
};
</script>

