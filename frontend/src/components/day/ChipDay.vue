<template>
  <v-chip
    :to="{ name: 'date', params: { date: day.month_day } }"
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



