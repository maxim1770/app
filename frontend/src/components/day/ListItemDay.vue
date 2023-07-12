<template>
  <v-list-item
    prepend-icon="mdi-calendar-range"
  >
    День Памяти:
    <ChipDay :day="day" class="ml-1" />
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



