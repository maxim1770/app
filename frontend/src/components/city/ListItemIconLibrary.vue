<template>
  <v-list-item
    prepend-icon="mdi-image-search-outline"
  >
    <v-chip
      @click="toUrl(icon.url)"
      color="teal-darken-2"
      class="ma-1"
    >
      Источник изображения Иконы
    </v-chip>
  </v-list-item>
</template>

<script>


import { toUrl } from "@/utils/common";

export default {
  props: {
    icon: {
      type: Object,
      required: true
    }
  },
  methods: { toUrl }
};

</script>



