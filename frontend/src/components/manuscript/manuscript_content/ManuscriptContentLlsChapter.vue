<template>
  <ManuscriptContentChapter
    v-if="hasNotLlsBookBookmarks"
    :manuscript="manuscript"
    :bookmarks="notLlsBookBookmarks"
    title="Избранное"
  />
  <ManuscriptContentChapter
    :manuscript="manuscript"
    :bookmarks="llsBookBookmarks"
    :isSecondManuscriptContent="hasNotLlsBookBookmarks"
  />
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import ChipChapter from "@/components/manuscript/ChipChapter.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";
import ManuscriptContentChapter from "@/components/manuscript/manuscript_content/ManuscriptContentChapter.vue";

export default {
  components: {
    ManuscriptContentChapter,
    BookmarkPageData,
    ChipChapter,
    MainSmallTitle,
    ManuscriptFullTitle,
    BookFullTitleFactory
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    llsBookBookmarks() {
      return Object.values(this.manuscript?.structured_bookmarks).filter(bookmark => bookmark.book.lls_book);
    },
    notLlsBookBookmarks() {
      return Object.values(this.manuscript?.structured_bookmarks).filter(bookmark => !bookmark.book.lls_book);
    },
    hasNotLlsBookBookmarks() {
      return this.notLlsBookBookmarks.length;
    }
  }
};

</script>
