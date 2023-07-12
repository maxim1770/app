<template>
  <div>
    <v-container
      v-for="week in cycle.weeks"
      :key="week.id"
      class="mb-2 rounded-lg border text-center"
    >
      <weekForCycle1And2 :week="week" />
    </v-container>
  </div>
</template>

<script>

import weekForCycle1And2 from "@/components/movable_date/week/weekForCycle1And2.vue";

export default {
  components: { weekForCycle1And2 },
  props: {
    cycle: {
      type: Object,
      required: true
    }
  }

};
</script>

