<template>
  <BookPage :book="book"/>
</template>

<script>
import {api} from "@/services/api";
import BookPage from "@/components/pages/BookPage.vue";

export default {
  components: {BookPage},

  data() {
    return {
      book: {
        type: Object,
        required: true,
      },
    };
  },
  watch: {
    $route(to, from) {
      this.getBook()
    }
  },
  mounted() {
    this.getBook()
  },
  methods: {
    getBook() {
      api
          .getBook(this.$route.params.bookId)
          .then((response) => (this.book = response.data));
    },
  },
};
</script>


