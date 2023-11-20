<template>
  <v-list-item
    v-if="tipikon"
    :prepend-icon="computeCustomIcon(tipikon.title_en)"
  >
    Типикон Праздника
    <ChipTipikon :tipikon="tipikon" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipTipikon from "@/components/holiday/tipikon/ChipTipikon.vue";
import { computeCustomIcon } from "@/utils/common";

export default {
  components: { ChipTipikon },
  props: {
    tipikon: {
      type: Object,
      required: true
    }
  },
  methods: { computeCustomIcon }
};

</script>


