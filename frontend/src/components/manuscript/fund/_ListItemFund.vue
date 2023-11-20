<template>
  <v-list-item
    prepend-icon="mdi-bookshelf"
  >
    Шифр
    <v-chip
      @click="toUrl(manuscript.url)"
      color="green"
      class="ma-1"
    >
      {{ manuscript?.fund.library }} {{ manuscript?.code_title }}
    </v-chip>
  </v-list-item>
</template>

<script>


import { toUrl } from "@/utils/common";

export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  methods: { toUrl }
};

</script>



