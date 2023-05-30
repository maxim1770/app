<template>
  <BooksPage :books="books"/>
</template>

<script>
import {api} from "@/services/api";
import BooksPage from "@/components/pages/BooksPage.vue";

export default {
  components: {BooksPage},

  data() {
    return {
      books: {
        type: Object,
        required: true,
      },
    };
  },

  mounted() {
    api
        .getBooks()
        .then((response) => (this.books = response.data));
  },
};
</script>
