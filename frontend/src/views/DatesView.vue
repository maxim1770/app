<template>
  <DatesPage :dates="dates" v-if="dates.dates?.[0]" />
</template>

<script>
import { api } from "@/services/api";
import DatesPage from "@/components/pages/DatesPage.vue";

export default {
  components: { DatesPage },

  data() {
    return {
      dates: {
        type: Array,
        required: true
      } // ref([])
    };
  },
  mounted() {
    api
      .getDates()
      .then((response) => (this.dates = response.data));
  }

};
</script>
