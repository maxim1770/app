<template>
  <v-list>
    <v-list-item
      :to="{name: 'book', params: { bookId: book.id } }"
      class="text-center mb-1"
    >
      <BookmarkPageData :bookmark="bookmark" />
      <BookFullTitleFactory :book="book" />
    </v-list-item>
    <v-divider />
    <ListItemManuscript :manuscript="bookmark?.manuscript" />
  </v-list>
</template>

<script>


import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import BookmarkPageData from "@/components/bookmark/BookmarkPageData.vue";

export default {
  components: { BookmarkPageData, BookFullTitleFactory, ListItemManuscript },
  props: {
    book: {
      type: Object,
      required: true
    },
    bookmark: {
      type: Object,
      required: true
    }
  }
};

</script>

