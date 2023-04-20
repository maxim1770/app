<template>
    <CyclePage :cycle="cycle"/>
</template>

<script>
import {api} from "@/api";
import CyclePage from "@/components/CyclePage.vue";

export default {
  components: {CyclePage},

  data() {
    return {
      cycle: {
        type: Object,
        required: true,
      },
    };
  },
  mounted() {
    api
      .getCycle(this.$route.params.cycleNum)
      .then((response) => (this.cycle = response.data));
  },
};
</script>


