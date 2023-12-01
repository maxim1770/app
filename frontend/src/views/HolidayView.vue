<template>
  <div>
    <HolidayPage
      v-if="holiday.id"
      :holiday="holiday"
    />
    <ChapterWithHead headTitle="Другие Праздники">
      <HolidaysView />
    </ChapterWithHead>
  </div>
</template>

<script>
import { api } from "@/services/api";
import HolidayPage from "@/components/pages/HolidayPage.vue";
import { numObjectKeys, replaceRouterQuery } from "@/utils/common";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import HolidaysView from "@/views/HolidaysView.vue";

export default {
  components: { HolidaysView, ChapterWithHead, HolidayPage },

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
    },
    holiday() {
      if (!numObjectKeys(this.$route.query)) {
        this.replaceRouterQuery({
          day__month: this.holiday.day?.month,
          day__day: this.holiday.day?.day
        });
      }
    }
  },
  mounted() {
    this.getHoliday();
  },
  methods: {
    replaceRouterQuery,
    getHoliday() {
      api
        .getHoliday(this.$route.params.holidaySlug)
        .then((response) => (this.holiday = response.data));
    }
  }
};
</script>
