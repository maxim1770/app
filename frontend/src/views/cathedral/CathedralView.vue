<template>
  <CathedralPage :cathedral="cathedral" />
</template>

<script>
import { api } from "@/services/api";
import CathedralPage from "@/components/pages/CathedralPage.vue";

export default {
  components: { CathedralPage },
  props: {
    cathedralSlug: {
      type: Object,
      required: false,
      default: null
    }
  },
  data() {
    return {
      cathedral: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getCathedral();
    }
  },
  mounted() {
    this.getCathedral();
  },
  methods: {
    getCathedral() {
      api
        .getCathedral(this.cathedralSlug || this.$route.params.cathedralSlug)
        .then((response) => (this.cathedral = response.data));
    }
  }
};
</script>
