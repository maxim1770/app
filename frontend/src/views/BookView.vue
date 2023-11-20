<template>
  <div>
    <BookPage
      v-if="book.book?.id"
      :book="book"
    />
    <BookSourceFactory
      v-if="book.book?.id"
      :key="BookSourceFactoryKeyForReRender"
      :book="book.book"
    />
    <ChapterWithHead
      headTitle="Другие Выдержки"
    >
      <BooksView />
    </ChapterWithHead>
  </div>
</template>

<script>
import { api } from "@/services/api";
import BookPage from "@/components/pages/BookPage.vue";
import { numObjectKeys, replaceRouterQuery } from "@/utils/common";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import BooksView from "@/views/BooksView.vue";
import BookSourceFactory from "@/components/book/book_source_factory/BookSourceFactory.vue";

export default {
  components: { BookSourceFactory, BooksView, ChapterWithHead, BookPage },

  data() {
    return {
      book: {
        type: Object,
        required: true
      },
      BookSourceFactoryKeyForReRender: 0
    };
  },
  computed: {
    topics__title__in() {
      let topics__title__in = [];
      for (let topic of this.book.book?.topic_book?.topics || []) {
        topics__title__in.push(topic.title);
      }
      return topics__title__in;
    }
  },
  watch: {
    $route(to, from) {
      this.getBook();
    },
    book() {
      if (!numObjectKeys(this.$route.query)) {
        this.replaceRouterQuery({
          topics__title__in: this.topics__title__in
        });
      }
      this.BookSourceFactoryKeyForReRender += 1;
    }
  },
  mounted() {
    this.getBook();
  },
  methods: {
    replaceRouterQuery,
    getBook() {
      api
        .getBook(this.$route.params.bookId)
        .then((response) => (this.book = response.data));
    }
  }
};
</script>


