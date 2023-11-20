<template>
  <v-list-item
    v-if="cathedral?.num_saints"
    prepend-icon="mdi-account-group-outline"
  >
    <ChipNumSaints :cathedral="cathedral" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipNumSaints from "@/components/cathedral/ChipNumSaints.vue";

export default {
  components: { ChipNumSaints },
  props: {
    cathedral: {
      type: Object,
      required: true
    }
  }
};

</script>



