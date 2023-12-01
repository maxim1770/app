<template>
  <div class="my-5">
    <ChapterWithHead
      :headTitle="book.zachalo ? 'Другие Зачала' : 'Другие Псалмы'"
    >
      <BibleBookView :bibleBookAbbr="bibleBookAbbr" />
    </ChapterWithHead>
  </div>
</template>

<script>


import BibleBookView from "@/views/bible_book/BibleBookView.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";

export default {
  components: { ChapterWithHead, BibleBookView },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    bibleBookAbbr() {
      return this.__some_book?.bible_book?.abbr;
    },
    __some_book() {
      return this.book?.zachalo || this.book?.psaltyr_book;
    }
  }
};

</script>
