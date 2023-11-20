<template>
  <div>
    <BibleBookView />
    <ChapterWithHead headTitle="Другие Книги">
      <BibleBooksView />
    </ChapterWithHead>
  </div>
</template>

<script>
import BibleBooksView from "@/views/BibleBooksView.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import BibleBookView from "@/views/bible_book/BibleBookView.vue";

export default {
  components: { BibleBookView, ChapterWithHead, BibleBooksView }

};
</script>
