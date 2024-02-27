<template>
  <v-chip
    v-if="tipikon"
    :to="{ name: 'holidays', query: {tipikon__title: tipikon.title} }"
    :prepend-icon="computeCustomIcon(tipikon.title_en)"
    color="red"
  >
    {{ tipikon.title }}
    <v-tooltip
      activator="parent"
    >
      Типикон Праздника определяется по Месяцесловам 16 в.
    </v-tooltip>
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
