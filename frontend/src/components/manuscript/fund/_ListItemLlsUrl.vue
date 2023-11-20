<template>
  <v-list-item
    prepend-icon="mdi-bookshelf"
  >
    Рукопись взята с сайта
    <ChipLlsUrl
      :manuscript_url="manuscript_url"
      class="ma-1"
    />
  </v-list-item>
</template>

<script>


import ChipLlsUrl from "@/components/manuscript/fund/ChipLlsUrl.vue";

export default {
  components: { ChipLlsUrl },
  props: {
    manuscript_url: {
      type: Object,
      required: true
    }
  }
};

</script>



