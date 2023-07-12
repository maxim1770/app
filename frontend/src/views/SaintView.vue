<template>
  <SaintPage :saint="saint" />
</template>

<script>
import { api } from "@/services/api";
import SaintPage from "@/components/pages/SaintPage.vue";

export default {
  components: { SaintPage },

  data() {
    return {
      saint: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getSaint();
    }
  },
  mounted() {
    this.getSaint();
  },
  methods: {
    getSaint() {
      api
        .getSaint(this.$route.params.saintSlug)
        .then((response) => (this.saint = response.data));
    }
  }

};
</script>
