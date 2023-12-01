<template>
  <ChapterWithHead
    v-memo="[movable_day?.week?.id]"
    headTitle="Чтения Священного Писания на неделю"
  >
    <template v-slot:head>
      <v-btn
        @click="$router.push({ name: 'movable-dates' })"
        prepend-icon="mdi-arrow-expand-right"
        variant="flat"
        size="small"
        color="blue-darken-2"
        class="text-none"
      >
        На весь год
      </v-btn>
    </template>
    <v-card>
      <v-container class="text-center mt-1">
        <CurrentWeekFactory
          :week="movable_day?.week"
          :currentMovableDayAbbr="movable_day?.abbr"
        />
      </v-container>
    </v-card>
  </ChapterWithHead>
</template>

<script>

import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import CurrentWeekFactory from "@/components/movable_date/week/CurrentWeekFactory.vue";

export default {
  components: { CurrentWeekFactory, ChapterWithHead },
  props: {
    movable_day: {
      type: Array,
      required: true
    }
  }

};
</script>
