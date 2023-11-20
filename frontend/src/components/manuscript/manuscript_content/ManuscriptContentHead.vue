<template>
  <ChapterWithHead
    headTitle="Содержание"
    class="mt-3"
  >
    <template v-slot:head>
      <UnfoldBtns @openAll="openAll" @closeAll="closeAll" />
    </template>
    <v-card>
      <v-card-item>
        <v-list
          v-model:opened="open"
          density="compact"
        >
          <v-list-group
            v-for="(subBookmarks, head_slug, index) in manuscript?.structured_bookmarks"
            :key="index"
            :value="head_slug"
          >
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                class="ma-1"
              >
                <HeadBookmarkFullTitleFactory :book="subBookmarks?.[0].book" />
              </v-list-item>
            </template>
            <v-list-item
              v-for="bookmark in subBookmarks"
              :key="bookmark.book.id"
              :to="{ name: 'book', params: { bookId: bookmark.book?.id } }"
            >
              <BookmarkPageData :bookmark="bookmark" class="ma-1" />
              <ChipChapter :chapter_num="bookmark?.chapter_num" class="ma-1" />
              <BookFullTitleFactory :book="bookmark?.book" />
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import HeadBookmarkFullTitleFactory from "@/components/book/HeadBookmarkFullTitleFactory.vue";
import UnfoldBtns from "@/components/common/UnfoldBtns.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ChipChapter from "@/components/manuscript/ChipChapter.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";

export default {
  components: {
    BookmarkPageData,
    ChipChapter,
    ChapterWithHead,
    UnfoldBtns,
    BookFullTitleFactory,
    HeadBookmarkFullTitleFactory
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      open: []
    };
  },
  methods: {
    openAll() {
      this.open = Object.keys(this.manuscript?.structured_bookmarks);
    },
    closeAll() {
      this.open = [];
    }
  }
};

</script>



