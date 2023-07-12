<template>
  <BibleBooksPage :bible_books="bible_books" />
</template>

<script>
import { api } from "@/services/api";
import BibleBooksPage from "@/components/pages/BibleBooksPage.vue";

export default {
  components: { BibleBooksPage },

  data() {
    return {
      bible_books: {
        type: Object,
        required: true
      }
    };
  },

  mounted() {
    api
      .getBibleBooks()
      .then((response) => (this.bible_books = response.data));
  }
};
</script>
