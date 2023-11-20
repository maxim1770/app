<template>
  <v-card
    v-for="week in cycle.weeks"
    :key="week.id"
    class="ma-4"
  >
    <v-container>
      <weekForCycle1And2 :week="week" />
    </v-container>
  </v-card>
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

