<template>
  <div class="mt-3">
    <MainSmallTitle title="Содержание" />
    <v-divider class="mt-1" />
    <v-timeline side="end" align="start">
      <v-timeline-item
        v-for="bookmark in manuscript?.structured_bookmarks"
        :key="bookmark?.id"
        @click="$router.push({ name: 'book', params: { bookId: bookmark.book?.id } })"
        dot-color="blue"
        icon="mdi-book-variant"
        fill-dot
        size="small"
      >
        <template v-if="lgAndUp" v-slot:opposite>
          <BookmarkPageData :bookmark="bookmark" />
        </template>
        <BookmarkPageData
          v-if="!lgAndUp"
          :bookmark="bookmark"
          class="ma-1"
        />
        <ChipChapter :chapter_num="bookmark?.chapter_num" class="ma-1" />
        <BookFullTitleFactory
          :book="bookmark?.book"
        />
      </v-timeline-item>
    </v-timeline>
    <v-divider />
  </div>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import { useDisplay } from "vuetify";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import ChipChapter from "@/components/manuscript/ChipChapter.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";

export default {
  components: { BookmarkPageData, ChipChapter, MainSmallTitle, ManuscriptFullTitle, BookFullTitleFactory },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>
