<template>
  <v-list-item
    prepend-icon="mdi-file-download-outline"
  >
    <BtnDownload :path="path" />
  </v-list-item>
</template>

<script>


import BtnDownload from "@/components/common/download/BtnDownload.vue";

export default {
  components: { BtnDownload },
  props: {
    path: {
      type: String,
      required: true
    }
  }
};

</script>



