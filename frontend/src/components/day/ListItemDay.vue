<template>
  <v-list-item
    v-if="day"
    prepend-icon="mdi-calendar-today-outline"
  >
    День Памяти
    <ChipDay
      :day="day"
      class="ma-1"
    />
  </v-list-item>
</template>

<script>


import ChipDay from "@/components/day/ChipDay.vue";

export default {
  components: { ChipDay },
  props: {
    day: {
      type: Object,
      required: true
    }
  }
};

</script>



