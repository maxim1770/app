<template>
  <v-sheet class="d-flex justify-center">
    <v-calendar
      @dayclick="toSelectedDate"
      :attributes="attributes"
      :columns="smAndDown ? 1 : 2"
      view="weekly"
      first-day-of-week="1"
    >
      <template #popover="{ event: { popover } }">{{ popover.description }}</template>
    </v-calendar>
  </v-sheet>
</template>

<script>


import { offsetYear2year } from "@/utils/date";
import { useDisplay } from "vuetify";

export default {
  props: {
    attributes: {
      type: Array,
      required: true
    }
  },
  setup() {
    const smAndDown = useDisplay();
    return smAndDown;
  },
  methods: {
    toSelectedDate(CalendarDay) {
      const year = offsetYear2year(CalendarDay.year, CalendarDay.month);
      this.$router.push({ name: "date", params: { dateSlug: CalendarDay.id.replace(CalendarDay.year, year) } });
    }
  }
};

</script>



