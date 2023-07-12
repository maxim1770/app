<template>
  <div>
    <v-container class="mb-2 rounded-lg border text-center">
      <v-row class="bg-red-lighten-3 border-b">
        <v-col
          cols="12"
          class="text-h6 text-red-accent-4 font-weight-bold"
        >
          Святой и Великий Пост
        </v-col>
      </v-row>
    </v-container>
    <v-container
      v-for="week in cycle.weeks.slice(0, -2)"
      :key="week.id"
      class="mb-2 rounded-lg border text-center"
    >
      <weekForCycle3 :week="week" />
    </v-container>
    <v-container
      class="mb-2 rounded-lg border text-center"
    >
      <week6InCycle3 :week="week6" />
    </v-container>
    <v-container class="mb-2 rounded-lg border text-center">
      <v-row class="bg-red-lighten-3 border-b">
        <v-col
          cols="12"
          class="text-h6 text-red-accent-4 font-weight-bold"
        >
          Страстная седмица
        </v-col>
      </v-row>
    </v-container>
    <v-container
      class="rounded-lg border text-center text-red-accent-3"
    >
      <strastnajaSedmitsa :week="strastnajaSedmitsa_" />
    </v-container>
  </div>
</template>

<script>

import ChipZachalo from "@/components/book/ChipZachalo.vue";
import weekForCycle3 from "@/components/movable_date/week/weekForCycle3.vue";
import week6InCycle3 from "@/components/movable_date/week/week6InCycle3.vue";
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";

export default {
  components: { ChipZachalo, weekForCycle3, week6InCycle3, strastnajaSedmitsa },
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

