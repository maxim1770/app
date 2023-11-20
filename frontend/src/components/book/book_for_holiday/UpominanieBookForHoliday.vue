<template>
  <ChapterWithHead
    v-if="upominanieBooks.length"
    headTitle="Упоминания"
  >
    <v-card
      v-for="holiday_book in upominanieBooks"
      :key="holiday_book.id"
      class="mb-3"
    >
      <GalleryMain :imgs_paths="computeBookmark(holiday_book)?.pages_paths" />
      <v-card-item>
        <v-list>
          <ListItemHolidayBookFullTitle :holiday_book="holiday_book" :holiday="holiday" :saint="saint" />
          <ListItemManuscript :manuscript="computeBookmark(holiday_book)?.manuscript" />
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>

import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";
import ListItemHolidayBookFullTitle from "@/components/book/book_full_title/list_item/ListItemHolidayBookFullTitle.vue";

export default {
  components: { ListItemHolidayBookFullTitle, GalleryMain, ListItemManuscript, ChapterWithHead },
  props: {
    upominanieBooks: {
      type: Array,
      required: true
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    },
    saint: {
      type: Object,
      required: false,
      default: null
    }
  },
  methods: {
    computeBookmark(holiday_book) {
      return holiday_book.book.bookmarks?.[0];
    }
  }

};
</script>