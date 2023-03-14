<template>
  <HolidaysPage :holidays="holidays"/>
</template>

<script>
import {api} from "@/api";
import HolidaysPage from "@/components/HolidaysPage.vue";

export default {
  components: {HolidaysPage},

  data() {
    return {
      holidays: {
        type: Object,
        required: true,
      },
    };
  },

  mounted() {
    api
        .getHolidays()
        .then((response) => (this.holidays = response.data));
  },
};
</script>
