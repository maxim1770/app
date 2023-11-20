<template>
  <v-list-item
    prepend-icon="mdi-check-circle-outline"
  >
    <ChipNumRules :cathedral="cathedral" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipNumRules from "@/components/cathedral/ChipNumRules.vue";

export default {
  components: { ChipNumRules },
  props: {
    cathedral: {
      type: Object,
      required: true
    }
  }
};

</script>



