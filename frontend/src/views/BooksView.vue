<template>
  <div>
    <ImgMainTitle
      mainPageValue="books"
      @click="$router.push({ name: 'books' })"
    />
    <CardRandomBook />
    <BooksPage :booksSearchData="booksSearchData" />
  </div>
</template>

<script>
import BooksPage from "@/components/pages/BooksPage.vue";
import { api } from "@/services/api";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";


export default {
  components: { ImgMainTitle, BooksPage, CardRandomBook },
  data() {
    return {
      booksSearchData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getBooksSearchData()
      .then((response) => (this.booksSearchData = response.data));
  }
};
</script>

