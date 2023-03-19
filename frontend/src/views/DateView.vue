<template>
  <DatePage :date="date"/>
</template>

<script>
import {api} from "@/api";
import DatePage from "@/components/DatePage.vue";

export default {
  components: {DatePage},

  data() {
    return {
      date: {
        type: Object,
        required: true,
      },
    };
  },

  mounted() {
    api
        .getDate(this.$route.params.date)
        .then((response) => (this.date = response.data));
  },
};
</script>
