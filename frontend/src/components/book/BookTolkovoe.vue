<template>
  <ChapterWithHead
    v-if="book_tolkovoe"
    headTitle="Толкование"
  >
    <CardBook :book="book_tolkovoe" :bookmark="bookmark" />
  </ChapterWithHead>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import CardBook from "@/components/book/CardBook.vue";

export default {
  components: { CardBook, ChapterWithHead },
  props: {
    book_tolkovoe: {
      type: Object,
      required: true
    }
  },
  computed: {
    bookmark() {
      return this.book_tolkovoe.bookmarks?.[0];
    }
  }
};

</script>



