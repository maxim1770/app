<template>
  <LlsPage :llsManuscripts="llsManuscripts" />
</template>

<script>
import { api } from "@/services/api";
import LlsPage from "@/components/pages/LlsPage.vue";

export default {
  components: { LlsPage },

  data() {
    return {
      llsManuscripts: {
        type: Object,
        required: true
      }
    };
  },

  mounted() {
    api
      .getLls()
      .then((response) => (this.llsManuscripts = response.data));
  }
};
</script>
