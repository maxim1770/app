<template>
  <v-chip
    v-if="tipikon"
    :prepend-icon="computeCustomIcon(tipikon.title_en)"
    color="red"
  >
    {{ tipikon.title }}
  </v-chip>
</template>

<script>


import { computeCustomIcon } from "@/utils/common";

export default {
  props: {
    tipikon: {
      type: Object,
      required: true
    }
  },
  methods: { computeCustomIcon }
};

</script>



