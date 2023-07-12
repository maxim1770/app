<template>
  <v-divider class="mt-1"></v-divider>
  <v-timeline side="end" align="start">
    <v-timeline-item
      v-for="bookmark in manuscript?.bookmarks_"
      :key="bookmark?.id"
      dot-color="blue"
      size="small"
    >
      <template v-slot:opposite>
        <router-link :to="{ name: 'book', params: { bookId: bookmark.book?.id } }">
          <ChipBookmarkFirstPageNum :first_page="bookmark.first_page" />
        </router-link>
      </template>
      <BookFullTitleFactory
        :book="bookmark?.book"
      />
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ChipBookmarkFirstPageNum from "@/components/manuscript/ChipBookmarkFirstPageNum.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";

export default {
  components: { ManuscriptFullTitle, BookFullTitleFactory, ChipBookmarkFirstPageNum },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>
