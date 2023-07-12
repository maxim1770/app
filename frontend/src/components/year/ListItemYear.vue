<template>
  <v-list-item
    prepend-icon="mdi-timer-sand"
  >
    Год:
    <ChipYear :year="year" class="ml-1" />
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



