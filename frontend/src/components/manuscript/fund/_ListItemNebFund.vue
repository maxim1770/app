<template>
  <span
    v-if="neb_url"
  >
    <v-list-item
      prepend-icon="mdi-bookshelf"
    >
      Рукопись на сайте библиотеки
      <v-chip
        @click="toUrl(neb_url)"
        color="blue-lighten-1"
        class="ma-1"
      >
        НЭБ
      </v-chip>
    </v-list-item>
    <v-divider class="my-1" />
  </span>
</template>

<script>


import { toUrl } from "@/utils/common";

export default {
  props: {
    neb_url: {
      type: Object,
      required: true
    }
  },
  methods: {
    toUrl
  }
};

</script>



