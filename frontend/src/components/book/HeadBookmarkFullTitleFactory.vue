<template>
  <component
    :is="headBookmarkFullTitleFactory"
    :book="book"
  />
</template>

<script>


import CathedralFullTitle from "@/components/cathedral/CathedralFullTitle.vue";
import BibleBookFullTitle from "@/components/bible_book/BibleBookFullTitle.vue";

export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    headBookmarkFullTitleFactory() {
      if (this.book?.cathedral_book) {
        return CathedralFullTitle;
      } else if (this.book?.zachalo || this.book?.psaltyr_book) {
        return BibleBookFullTitle;
      }
    }
  }
};
</script>

