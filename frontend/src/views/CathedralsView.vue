<template>
  <CathedralsPage :cathedrals="cathedrals"/>
</template>

<script>
import {api} from "@/services/api";
import CathedralsPage from "@/components/pages/CathedralsPage.vue";

export default {
  components: {CathedralsPage},

  data() {
    return {
      cathedrals: {
        type: Object,
        required: true,
      },
    };
  },

  mounted() {
    api
      .getCathedrals()
      .then((response) => (this.cathedrals = response.data));
  },
};
</script>
