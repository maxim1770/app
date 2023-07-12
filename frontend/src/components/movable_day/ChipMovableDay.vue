<template>
  <v-chip
    variant="tonal"
    color="amber"
    prepend-icon="mdi-calendar-today-outline"
    v-if="movable_day?.month_day"
    :to="{ name: 'date', params: { date: movable_day.month_day } }"
  >
    {{ movable_day?.full_title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    movable_day: {
      type: Object,
      required: true
    }
  }
};

</script>



