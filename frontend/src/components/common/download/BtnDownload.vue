<template>
  <v-btn
    :href="imgUrl(path)"
    prepend-icon="mdi-file-download-outline"
    color="light-green-accent-4"
    variant="tonal"
    size="small"
    rounded="lg"
  >
    Скачать
  </v-btn>
</template>


<script>


import { imgUrl } from "@/utils/common";

export default {
  props: {
    path: {
      type: String,
      required: true
    }
  },
  methods: { imgUrl }
};

</script>



