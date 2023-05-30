<template>
  <div>
    <CycleNum1And2 :cycle="movableDates[0]" />
    <CycleNum1And2 :cycle="movableDates[1]" />
    <CycleNum3 :cycle="movableDates[2]" />
  </div>
</template>

<script>

import CycleNum1And2 from "@/components/movable_date/CycleNum1And2.vue";
import CycleNum3 from "@/components/movable_date/CycleNum3.vue";

export default {

  components: { CycleNum1And2, CycleNum3 },

  props: {
    movableDates: {
      type: Object,
      required: true
    }
  }
};
</script>

