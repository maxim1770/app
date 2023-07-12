<template>
  <v-list
    density="compact"
    lines="one"
  >
    <v-list-group
      v-for="(subBookmarks, head_slug, index) in manuscript?.bookmarks_"
      :key="index"
    >
      <template v-slot:activator="{ props }">
        <v-list-item
          v-bind="props"
          rounded="lg"
        >
          <v-list-item-title class="text-body-2 font-weight-bold">
            <HeadBookmarkFullTitleFactory :book="subBookmarks?.[0].book" />

          </v-list-item-title>
        </v-list-item>
      </template>
      <v-list-item
        v-for="bookmark in subBookmarks"
        :key="bookmark.book.id"
        :to="{ name: 'book', params: { bookId: bookmark.book?.id } }"
        rounded="xl"
      >
        <div class="mb-1">
          <ChipBookmarkFirstPageNum :first_page="bookmark.first_page" class="mr-1" />
          <BookFullTitleFactory :book="bookmark?.book" />
        </div>
        <v-divider></v-divider>
      </v-list-item>
    </v-list-group>
  </v-list>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ChipBookmarkFirstPageNum from "@/components/manuscript/ChipBookmarkFirstPageNum.vue";
import HeadBookmarkFullTitleFactory from "@/components/book/head_bookmark_full_title/HeadBookmarkFullTitleFactory.vue";

export default {
  components: { BookFullTitleFactory, ChipBookmarkFirstPageNum, HeadBookmarkFullTitleFactory },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



