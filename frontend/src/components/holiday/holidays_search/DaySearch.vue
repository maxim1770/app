<template>
  <div class="text-center">
    <p class="mb-2 text-body-1 font-weight-bold">День Памяти</p>
    <v-date-picker
      @update:modelValue="updateDay"
      :model-value="selectedDate"
      :masks="CALENDAR_MASKS"
      first-day-of-week="1"
    />
  </div>
</template>


<script>


import { CALENDAR_MASKS, getMonth, offsetYear2year } from "@/utils/date";
import { replaceRouterQuery } from "@/utils/common";

export default {
  props: {
    day__month: {
      type: Number,
      required: true
    },
    day__day: {
      type: Number,
      required: true
    }
  },
  computed: {
    selectedDate() {
      return new Date(
        offsetYear2year(new Date().getFullYear(), this.day__month),
        this.day__month - 1,
        this.day__day
      );
    },
    CALENDAR_MASKS() {
      return CALENDAR_MASKS;
    }
  },
  methods: {
    replaceRouterQuery,
    updateDay(event) {
      this.replaceRouterQuery({
        day__day: event.getDate(),
        day__month: getMonth(event)
      });
    }
  }
};

</script>

