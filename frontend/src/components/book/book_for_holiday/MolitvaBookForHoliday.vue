<template>
  <ChapterWithHead
    v-if="numObjectKeys(molitva_books_by_manuscript)"
    headTitle="Тропари, Кондаки"
  >
    <v-card
      v-for="(molitva_books, manuscript_code, index) in molitva_books_by_manuscript"
      :key="index"
      class="mb-3"
    >
      <GalleryMain :imgs_paths="manuscriptJoinedPagesPaths(molitva_books)" />
      <v-card-item>
        <v-list>
          <v-list-item
            v-for="molitva_book in molitva_books"
            :key="molitva_book.id"
            :to="{ name: 'book', params: { bookId: molitva_book.id } }"
          >
            <template v-slot:prepend>
              <v-icon
                icon="mdi-book-open-variant"
                :color="choiceHolidayColor(molitva_book.holiday)"
              />
            </template>
            <MolitvaBookFullTitle :book="molitva_book.book" :molitva_book="molitva_book" :holiday="holiday" />
          </v-list-item>
          <v-divider class="my-1" />
          <ListItemManuscript :manuscript="computeBookmark(molitva_books).manuscript" />
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>

import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";
import BadgeNum from "@/components/common/BadgeNum.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";
import MolitvaBookFullTitle from "@/components/book/book_full_title/MolitvaBookFullTitle.vue";
import { choiceHolidayColor } from "@/utils/holidays";
import { numObjectKeys } from "@/utils/common";

export default {
  components: {
    GalleryMain,
    BadgeNum,
    HolidayFullTitle,
    ListItemManuscript,
    ChapterWithHead,
    MolitvaBookFullTitle
  },
  props: {
    molitva_books_by_manuscript: {
      type: Object,
      required: true
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    }
  },
  methods: {
    numObjectKeys,
    choiceHolidayColor,
    manuscriptJoinedPagesPaths(molitva_books) {
      const manuscriptJoinedPagesPaths = new Set();
      molitva_books?.forEach((molitva_book) => {
        this.__computeBookmark(molitva_book)?.pages_paths.forEach(
          page_path => {
            manuscriptJoinedPagesPaths.add(page_path);
          });
      });
      return manuscriptJoinedPagesPaths;
    },
    computeBookmark(molitva_books) {
      return this.__computeBookmark(molitva_books?.[0]);
    },
    __computeBookmark(molitva_book) {
      return molitva_book.book?.bookmarks?.[0];
    }
  }

};
</script>