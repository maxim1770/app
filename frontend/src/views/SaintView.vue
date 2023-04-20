<template>
    <SaintPage :saint="saint"/>
</template>

<script>
import {api} from "@/api";
import SaintPage from "@/components/SaintPage.vue";

export default {
  components: {SaintPage},

  data() {
    return {
      saint: {
        type: Object,
        required: true,
      },
    };
  },
  mounted() {
      api
          .getSaint(this.$route.params.saintSlug)
          .then((response) => (this.saint = response.data));
  },
};
</script>
