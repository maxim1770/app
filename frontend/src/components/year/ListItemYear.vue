<template>
  <v-list-item
    v-if="year"
    prepend-icon="mdi-timer-sand"
  >
    Год
    <ChipYear :year="year" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";

export default {
  components: { ChipYear },
  props: {
    year: {
      type: Object,
      required: true
    }
  }
};

</script>



