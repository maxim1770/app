<template>
  <HolidayPage :holiday="holiday"/>
</template>

<script>
import {api} from "@/api";
import HolidayPage from "@/components/HolidayPage.vue";

export default {
  components: {HolidayPage},

  data() {
    return {
      holiday: {
        type: Object,
        required: true,
      },
    };
  },

  mounted() {
    api
        .getHoliday(this.$route.params.holidaySlug)
        .then((response) => (this.holiday = response.data));
  },
};
</script>
