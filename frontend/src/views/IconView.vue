<template>
  <IconPage v-if="icon.id" :icon="icon" />
</template>

<script>
import { api } from "@/services/api";
import IconPage from "@/components/pages/IconPage.vue";

export default {
  components: { IconPage },

  data() {
    return {
      icon: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getIcon();
    }
  },
  mounted() {
    this.getIcon();
  },
  methods: {
    getIcon() {
      api
        .getIcon(this.$route.params.iconId)
        .then((response) => (this.icon = response.data));
    }
  }
};
</script>
