<template>
  {{ bibleBook.title }}
</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    bibleBook() {
      return this.book.zachalo.bible_book;
    }
  }
};

</script>



