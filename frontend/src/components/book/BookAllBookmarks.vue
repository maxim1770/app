<template>
  <ChapterWithHead
    v-if="allBookmarks.length"
    headTitle="Читать в других Рукописях"
  >
    <CardBook
      v-for="bookmark in allBookmarks"
      :key="bookmark.manuscript.id"
      :bookmark="bookmark"
      :book="book"
      class="mb-3"
    />
  </ChapterWithHead>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import CardBook from "@/components/book/CardBook.vue";

export default {
  components: { CardBook, ChapterWithHead },
  props: {
    allBookmarks: {
      type: Array,
      required: true
    },
    book: {
      type: Array,
      required: true
    }
  }
};

</script>



