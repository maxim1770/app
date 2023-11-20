<template>
  <div class="my-5">
    <ChapterWithHead headTitle="Другие Правила">
      <CathedralView :cathedralSlug="book?.cathedral_book.cathedral?.slug" />
    </ChapterWithHead>
  </div>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import CathedralView from "@/views/cathedral/CathedralView.vue";

export default {
  components: { CathedralView, ChapterWithHead },
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>



