<template>
  <v-chip
    @click="toUrl(manuscript_url)"
    color="green"
  >
    «Руниверс»
  </v-chip>
</template>

<script>


import { toUrl } from "@/utils/common";

export default {
  props: {
    manuscript_url: {
      type: Object,
      required: true
    }
  },
  methods: { toUrl }
};

</script>

