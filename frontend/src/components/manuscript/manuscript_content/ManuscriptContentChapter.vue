<template>
  <div
    :class="isSecondManuscriptContent ? 'mt-1' : 'mt-3'"
  >
    <MainSmallTitle
      :title="title || 'Содержание'"
      :textColor="title ? 'red-darken-3' : 'black'"
    />
    <v-divider class="mt-1" />
    <v-timeline side="end" align="start">
      <v-timeline-item
        v-for="bookmark in Bookmarks"
        :key="bookmark?.id"
        @click="$router.push({ name: 'book', params: { bookId: bookmark.book?.id } })"
        :dot-color="title ? 'red-lighten-1' : 'blue'"
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
    },
    bookmarks: {
      type: Object,
      required: false,
      default: null
    },
    title: {
      type: String,
      required: false,
      default: null
    },
    isSecondManuscriptContent: {
      type: Boolean,
      required: false,
      default: false
    }
  },
  computed: {
    Bookmarks() {
      return this.bookmarks || this.manuscript?.structured_bookmarks;
    }

  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>
