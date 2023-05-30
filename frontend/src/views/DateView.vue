<template>
  <div class="d-block">
    <v-btn
      @click=foo
      class="d-flex w-100 justify-center mb-5 mt-2 align-center text-center"
      :class="{
                        'bg-green-lighten-3': date.day?.has_new_holidays
                    }"
    >
      test
    </v-btn>
    <DatePage :date="date" />
  </div>
</template>

<script>
import { api } from "@/services/api";
import { nextDate } from "@/utils/date";
import DatePage from "@/components/pages/DatePage.vue";

export default {
  components: { DatePage },

  data() {
    return {
      date: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getDate();
    }
  },
  mounted() {
    this.getDate();
  },
  methods: {
    getDate() {
      api
        .getDate(this.$route.params.date)
        .then((response) => (this.date = response.data));
    },
    foo() {
      if (this.date.day?.has_new_holidays === false) {
        this.$router.push({ name: "date", params: { date: nextDate(this.date.day?.month_day) } });
      }
    }
  }
};
</script>
