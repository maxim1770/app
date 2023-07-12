<template>
  <v-list
    density="compact"
    lines="one"
  >
    <v-list-group
      v-for="(days_nums_dict, month_num, index) in manuscript?.bookmarks_"
      :key="index"

    >
      <template v-slot:activator="{ props }">
        <v-list-item
          v-bind="props"
        >
          <v-list-item-title class="text-body-2 font-weight-bold">{{ monthTitle(month_num) }}</v-list-item-title>
        </v-list-item>
      </template>
      <v-list-group
        v-for="(bookmarks, day_num, index) in days_nums_dict"
        :key="index"
      >
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
          >
            <v-list-item-title class="font-weight-bold">{{ day_num }}</v-list-item-title>
          </v-list-item>
        </template>
        <v-list-item
          v-for="bookmark in bookmarks"
          :key="bookmark.book.id"
          :to="{ name: 'book', params: { bookId: bookmark.book?.id } }"
        >
          <div class="mb-1">
            <ChipBookmarkFirstPageNum :first_page="bookmark.first_page" class="mr-1" />
            <BookFullTitleFactory :book="bookmark?.book" />
          </div>
          <v-divider></v-divider>
        </v-list-item>
      </v-list-group>
    </v-list-group>
  </v-list>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ChipBookmarkFirstPageNum from "@/components/manuscript/ChipBookmarkFirstPageNum.vue";
import { MONTH_TITLE } from "@/utils/common";

export default {
  components: { BookFullTitleFactory, ChipBookmarkFirstPageNum },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  methods: {
    monthTitle(monthNum) {
      return MONTH_TITLE[monthNum];
    }
  }
};

</script>



