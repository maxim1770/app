<template>
  <div>
    <ImgMainTitle
      mainPageValue="bible-books"
      @click="$router.push({ name: 'bible-books' })"
    />
    <BibleBooksPage :bible_books="bible_books" />
    <CardRandomBook />
  </div>
</template>

<script>
import { api } from "@/services/api";
import BibleBooksPage from "@/components/pages/BibleBooksPage.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";

export default {
  components: { CardRandomBook, ImgMainTitle, BibleBooksPage },

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
