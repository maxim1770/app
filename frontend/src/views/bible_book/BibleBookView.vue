<template>
  <BibleBookPage :bible_book="bible_book" />
</template>

<script>
import { api } from "@/services/api";
import BibleBookPage from "@/components/pages/BibleBookPage.vue";

export default {
  components: { BibleBookPage },
  props: {
    bibleBookAbbr: {
      type: Object,
      required: false,
      default: null
    }
  },
  data() {
    return {
      bible_book: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getBibleBook();
    }
  },
  mounted() {
    this.getBibleBook();
  },
  methods: {
    getBibleBook() {
      api
        .getBibleBook(this.bibleBookAbbr || this.$route.params.bibleBookAbbr)
        .then((response) => (this.bible_book = response.data));
    }
  }
};
</script>
