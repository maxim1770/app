<template>
  <v-chip
    v-if="movable_day"
    :to="{ name: 'date', params: { dateSlug: movable_day?.date_slug } }"
    color="amber"
    prepend-icon="mdi-calendar-today-outline"
  >
    {{ isSunDate ? sundayTitle : movable_day?.title || movable_day?.full_title }}
  </v-chip>
</template>

<script>


import { isSunDate } from "@/utils/date";

export default {
  props: {
    movable_day: {
      type: Object,
      required: true
    }
  },
  computed: {
    isSunDate() {
      return isSunDate({ "movable_day": this.movable_day });
    },
    sundayTitle() {
      return this.movable_day?.sunday_title || this.movable_day?.week?.sunday_title || this.movable_day?.full_title;
    }
  }
};

</script>


