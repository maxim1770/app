<template>
  <v-chip
    :to="{ name: 'date', params: { date: day.month_day } }"
    variant="tonal"
    color="amber"
    prepend-icon="mdi-calendar-today-outline"
  >
    {{ day.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    day: {
      type: Object,
      required: true
    }
  }
};

</script>



