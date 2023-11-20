<template>
  <v-container>
    <v-row
      v-for="i in this.books?.length"
      :key="i"
    >
      <template v-if="i % 2 === 1">
        <v-col
          v-for="book in this.books.slice(i-1, i +1)"
          :key="book.id"
          cols="12"
          sm="12"
          :lg="6 ? this.books?.length > 1 : 12"
          align="center"
        >
          <CardBook
            :bookmark="computeBookmark(book)"
            :book="book"
          />
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script>


import { imgUrl } from "@/utils/common";
import CardBook from "@/components/book/CardBook.vue";

export default {
  components: {
    CardBook
  },
  props: {
    books: {
      type: Array,
      required: true
    }
  },
  methods: {
    imgUrl,
    computeBookmark(book) {
      return book.bookmarks?.[0];
    }
  }
};
</script>



