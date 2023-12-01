<template>
  <component
    :is="manuscriptContentFactory"
    :manuscript="manuscript"
  />
</template>

<script>


import ManuscriptContentDate from "@/components/manuscript/manuscript_content/ManuscriptContentDate.vue";
import ManuscriptContentChapter from "@/components/manuscript/manuscript_content/ManuscriptContentChapter.vue";
import ManuscriptContentHead from "@/components/manuscript/manuscript_content/ManuscriptContentHead.vue";
import ManuscriptContentLlsChapter from "@/components/manuscript/manuscript_content/ManuscriptContentLlsChapter.vue";

export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    manuscriptContentFactory() {
      if (this.__isArrayWithArrayValues(this.manuscript?.structured_bookmarks)) {
        return ManuscriptContentDate;
      } else if (this.__isDictWithArrayValues(this.manuscript?.structured_bookmarks)) {
        return ManuscriptContentHead;
      } else if (this.__hasLlsBookBookmark(this.manuscript?.structured_bookmarks)) {
        return ManuscriptContentLlsChapter;
      } else {
        return ManuscriptContentChapter;
      }
    }
  },
  methods: {
    __isDictWithArrayValues(obj) {
      if (typeof obj !== "object" || obj === null) {
        return false;
      }
      for (const key in obj) {
        if (Array.isArray(obj[key]) === false) {
          return false;
        }
      }
      return true;
    },
    __isArrayWithArrayValues(obj) {
      if (Array.isArray(obj) === false || obj === null) {
        return false;
      }
      for (const key in obj) {
        if (Array.isArray(obj[key]) === false) {
          return false;
        }
      }
      return true;
    },
    __hasLlsBookBookmark(bookmarks) {
      if (bookmarks.find(bookmark => bookmark.book.lls_book)) {
        return true;
      }
      return false;
    }
  }
};

</script>

