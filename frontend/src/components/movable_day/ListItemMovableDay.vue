<template>
  <v-list-item
    prepend-icon="mdi-calendar-range"
  >
    Переходящая дата:
    <ChipMovableDay :movable_day="movable_day" class="ml-1" />
  </v-list-item>
</template>

<script>


import ChipMovableDay from "@/components/movable_day/ChipMovableDay.vue";

export default {
  components: { ChipMovableDay },
  props: {
    movable_day: {
      type: Object,
      required: true
    }
  }
};

</script>



