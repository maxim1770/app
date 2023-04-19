<template>
  <DatesPage :dates="dates"/>
</template>

<script>
import {api} from "@/api";
import DatesPage from "@/components/DatesPage.vue";

export default {
  components: {DatesPage},

  data() {
    return {
      dates: {
        type: Array,
        required: true,
      }, // ref([])
    };
  },
  created() {
    api
      .getDates()
      .then((response) => (this.dates = response.data));
  },
};
</script>
