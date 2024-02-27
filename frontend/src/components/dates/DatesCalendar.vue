<template>
  <v-sheet
    v-memo="[year]"
    elevation="6"
    rounded="xl"
    class="text-center mt-5"
  >
    <v-calendar
      :masks="CALENDAR_MASKS"
      :initial-page="{ month: 9, year: calendarInitialYear }"
      :attributes="dates.attributes"
      :rows="numRows"
      :columns="numColumns"
      first-day-of-week="1"
      @dayclick="toSelectedDate"
      @update:pages="updateYear"
      class="w-100"
    >
      <template #popover="{ event: { popover } }">{{ popover.description }}</template>
    </v-calendar>
  </v-sheet>
</template>

<script>


import { CALENDAR_MASKS, offsetYear2year, year2offsetYear } from "@/utils/date";
import { useDisplay } from "vuetify";

export default {
  props: {
    dates: {
      type: Object,
      required: true
    },
    year: {
      type: Number,
      required: true
    }
  },
  emits: [
    "update:year"
  ],
  computed: {
    numRows() {
      if (this.smAndDown) {
        return 12;
      } else if (this.lgAndDown) {
        return 6;
      }
      return 4;
    },
    numColumns() {
      if (this.smAndDown) {
        return 1;
      } else if (this.lgAndDown) {
        return 2;
      }
      return 3;
    },
    calendarInitialYear() {
      return year2offsetYear(this.year, 9);
    },
    CALENDAR_MASKS() {
      return CALENDAR_MASKS;
    }
  },
  setup() {
    const { smAndDown, lgAndDown } = useDisplay();
    return { smAndDown, lgAndDown };
  },
  methods: {
    toSelectedDate(CalendarDay) {
      const year = offsetYear2year(CalendarDay.year, CalendarDay.month);
      this.$router.push(
        {
          name: "date",
          params: {
            dateSlug: CalendarDay?.id.replace(CalendarDay.year, year)
          }
        }
      );
    },
    updateYear(page) {
      if (Number(this.year) === offsetYear2year(page[0]?.year, 9)) {
      } else if (Number(this.year) < offsetYear2year(page[0]?.year, 9)) {
        this.$emit("update:year", Number(this.year) + 1);
      } else {
        this.$emit("update:year", Number(this.year) - 1);
      }
    }
  }
};

</script>
