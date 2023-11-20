<template>
  <v-chip
    v-if="movable_day"
    :to="{ name: 'date', params: { dateSlug: movable_day.date_slug } }"
    color="amber"
    prepend-icon="mdi-calendar-today-outline"
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



