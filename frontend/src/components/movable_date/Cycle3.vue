<template>
  <v-card class="bg-red-lighten-3 ma-3">
    <v-container>
      <v-row>
        <v-col class="text-h6 text-red-accent-4 font-weight-bold">
          Святой и Великий Пост
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  <v-card
    v-for="week in cycle.weeks.slice(0, -2)"
    :key="week.id"
    class="ma-4"
  >
    <v-container>
      <weekForCycle3 :week="week" />
    </v-container>
  </v-card>
  <v-card class="ma-4">
    <v-container>
      <week6InCycle3 :week="week6" />
    </v-container>
  </v-card>
  <v-card class="bg-red-lighten-3 ma-3">
    <v-container>
      <v-row>
        <v-col class="text-h6 text-red-accent-4 font-weight-bold">
          Страстная седмица
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  <v-card class="text-red-accent-3 ma-4">
    <v-container>
      <strastnajaSedmitsa :week="strastnajaSedmitsa_" />
    </v-container>
  </v-card>
</template>

<script>

import weekForCycle3 from "@/components/movable_date/week/weekForCycle3.vue";
import week6InCycle3 from "@/components/movable_date/week/week6InCycle3.vue";
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";

export default {
  components: { weekForCycle3, week6InCycle3, strastnajaSedmitsa },
  props: {
    cycle: {
      type: Object,
      required: true
    }
  },
  computed: {
    week6() {
      return this.cycle.weeks[5];
    },
    strastnajaSedmitsa_() {
      return this.cycle.weeks[6];
    }
  }
};
</script>

