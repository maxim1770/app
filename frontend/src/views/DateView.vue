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
  watch: {
    $route(to, from) {
      this.getDate()
    }
  },
  mounted() {
    this.getDate()
  },
  methods: {
    getDate() {
      api
          .getDate(this.$route.params.date)
          .then((response) => (this.date = response.data));
    },
  },
};
</script>
