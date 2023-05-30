<template>
    <DatesPage :dates="dates"/>
</template>

<script>
import {api} from "@/services/api";
import DatesPage from "@/components/pages/DatesPage.vue";

export default {
  components: {DatesPage},

  data() {
    return {
      dates: {
        type: Object,
        required: true,
      }, // ref([])
    };
  },
  mounted() {
    api
      .getDates()
      .then((response) => (this.dates = response.data));
  },

};
</script>
