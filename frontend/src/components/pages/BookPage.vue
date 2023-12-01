<template>
  <div
    v-memo="[book.book?.id]"
  >
    <CardBook
      :bookmark="bookmarkWithBestManuscriptHandwriting"
      :book="this.book.book"
    />
    <!--    <AdminPutBookmarkPages :book="this.book.book" />-->
    <BookTolkovoe
      :key="BookTolkovoeKeyForReRender"
      :book_tolkovoe="book.book_tolkovoe"
    />
    <BookAllBookmarks
      :allBookmarks="allBookmarks"
      :book="this.book.book"
    />
  </div>
</template>

<script>
import BookTolkovoe from "@/components/book/BookTolkovoe.vue";
import BookAllBookmarks from "@/components/book/BookAllBookmarks.vue";
import AdminPutBookmarkPages from "@/components/book/AdminPutBookmarkPages.vue";
import CardBook from "@/components/book/CardBook.vue";
import ManuscriptsView from "@/views/ManuscriptsView.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";


export default {
  components: {
    ChapterWithHead, ManuscriptsView,
    CardBook,
    AdminPutBookmarkPages,
    BookAllBookmarks,
    BookTolkovoe
  },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      BookTolkovoeKeyForReRender: 0
    };
  },
  computed: {
    bookmarkWithBestManuscriptHandwriting() {
      return Object.assign([], this.book.book?.bookmarks).sort((b1, b2) => b1.manuscript?.handwriting < b2.manuscript?.handwriting ? 1 : -1)[0];
    },
    allBookmarks() {
      return Object.assign([], this.book.book?.bookmarks).sort((b1, b2) => b1.manuscript?.handwriting < b2.manuscript?.handwriting ? 1 : -1).slice(1);
    }
  },
  watch: {
    book() {
      this.BookTolkovoeKeyForReRender += 1;
    }
  }
};
</script>

