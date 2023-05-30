<template>
    <HolidaysPage :holidays="holidays"/>
</template>

<script>
import {api} from "@/services/api";
import HolidaysPage from "@/components/pages/HolidaysPage.vue";

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
