<template>
  <v-chip
    v-if="day"
    :to="{ name: 'date', params: { dateSlug: day.date_slug } }"
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



