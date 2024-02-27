<template>
  <v-card class="bg-red-lighten-3 ma-3">
    <v-container>
      <v-row>
        <v-col>
          <MainSmallTitle
            title="Святой и Великий Пост"
            text-color="red-accent-4"
            :hasMargin="false"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-card>
  <v-card
    class="ma-4"
  >
    <v-container>
      <week1InCycle3
        :week="cycle.weeks[6]"
      />
    </v-container>
  </v-card>
  <v-card
    v-for="week in [cycle.weeks[0], cycle.weeks[1], cycle.weeks[2], cycle.weeks[3], cycle.weeks[4]]"
    :key="week.id"
    class="ma-4"
  >
    <v-container>
      <weekForCycle3 :week="week" />
    </v-container>
  </v-card>
  <v-card class="ma-4">
    <v-container>
      <sun6InCycle3
        :week="strastnajaSedmitsa_"
      />
    </v-container>
  </v-card>
  <v-card class="bg-red-lighten-3 ma-3">
    <v-container>
      <v-row>
        <v-col>
          <MainSmallTitle
            title="Страстная седмица"
            text-color="red-accent-4"
            :hasMargin="false"
          />
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
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";
import Week1InCycle3 from "@/components/movable_date/week/week1InCycle3.vue";
import Sun6InCycle3 from "@/components/movable_date/week/sun6InCycle3.vue";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle, Sun6InCycle3, Week1InCycle3, weekForCycle3, strastnajaSedmitsa },
  props: {
    cycle: {
      type: Object,
      required: true
    }
  },
  computed: {
    strastnajaSedmitsa_() {
      return this.cycle.weeks[5];
    }
  }
};
</script>
