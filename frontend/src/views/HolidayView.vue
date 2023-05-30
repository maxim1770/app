<template>
  <HolidayPage :holiday="holiday" />
</template>

<script>
import { api } from "@/services/api";
import HolidayPage from "@/components/pages/HolidayPage.vue";

export default {
  components: { HolidayPage },

  data() {
    return {
      holiday: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getHoliday();
    }
  },
  mounted() {
    this.getHoliday();
  },
  methods: {
    getHoliday() {
      api
        .getHoliday(this.$route.params.holidaySlug)
        .then((response) => (this.holiday = response.data));
    }
  }
};
</script>
