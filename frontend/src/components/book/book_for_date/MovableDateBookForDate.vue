<template>
  <ChapterWithHead
    v-if="movable_date_books?.length"
    headTitle="Чтения по времени"
  >
    <v-card
      v-for="movable_date_book in movable_date_books"
      :key="movable_date_book.id"
      class="mb-3"
    >
      <GalleryMain :imgs_paths="computeBookmark(movable_date_book)?.pages_paths" />
      <v-card-item>
        <v-list>
          <ListItemMovableDateBookFullTitle :movable_date_book="movable_date_book" />
          <ListItemManuscript :manuscript="computeBookmark(movable_date_book)?.manuscript" />
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>

import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";
import ListItemMovableDateBookFullTitle
  from "@/components/book/book_full_title/list_item/ListItemMovableDateBookFullTitle.vue";

export default {
  components: { ListItemMovableDateBookFullTitle, GalleryMain, ChapterWithHead, ListItemManuscript },
  props: {
    movable_date_books: {
      type: Array,
      required: true
    }
  },
  methods: {
    computeBookmark(movable_date_book) {
      return movable_date_book?.book?.bookmarks?.[0];
    }
  }
};
</script>