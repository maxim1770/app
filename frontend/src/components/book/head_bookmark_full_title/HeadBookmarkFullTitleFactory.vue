<template>
  <component
    :is="headBookmarkFullTitleFactory"
    :book="book"
  />
</template>

<script>

import BibleBookFullTitle from "@/components/book/head_bookmark_full_title/BibleBookFullTitle.vue";
import CathedralFullTitle from "@/components/book/head_bookmark_full_title/CathedralFullTitle.vue";

export default {
  components: {
    CathedralFullTitle, BibleBookFullTitle
  },
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
      } else if (this.book?.zachalo) {
        return BibleBookFullTitle;
      }
    }
  }
};
</script>

