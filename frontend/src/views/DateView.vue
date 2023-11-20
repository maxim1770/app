<template>
  <DatePage v-if="date.year" :date="date" />
</template>

<script>
import { api } from "@/services/api";
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
        .getDate(this.$route.params.dateSlug)
        .then((response) => (this.date = response.data));
    }
  }
};
</script>
