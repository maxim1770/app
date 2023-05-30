<template>
  <ManuscriptPage :manuscript="manuscript" />
</template>

<script>
import { api } from "@/services/api";
import ManuscriptPage from "@/components/pages/ManuscriptPage.vue";

export default {
  components: { ManuscriptPage },

  data() {
    return {
      manuscript: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getManuscript();
    }
  },
  mounted() {
    this.getManuscript();
  },
  methods: {
    getManuscript() {
      api
        .getManuscript(this.$route.params.manuscriptCode)
        .then((response) => (this.manuscript = response.data));
    }
  }
};
</script>
