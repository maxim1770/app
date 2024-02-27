<template>
  <div
    v-memo="[sorted_bible_books?.length]"
  >
    <v-divider />
    <MainTitle title="Новый Завет" textColor="red-darken-4" :hasDivider="true" />
    <template
      v-for="bible_books in [evangelies, apostols]"
      :key="bible_books?.[0]?.id"
    >
      <MainTitle
        v-if="bible_books?.[0]?.part_ru"
        :title="bible_books[0].part_ru"
        textColor="red-darken-3"
        :hasDivider="true"
      />
      <TimelineBibleBooks :bible_books="bible_books" />
      <v-divider />
    </template>
    <MainTitle title="Ветхий Завет" textColor="red-darken-4" :hasDivider="true" />
    <template
      v-for="bible_books in [pjatiknizhieMoiseja, psaltyr, oldTestamentOtherBibleBooks]"
      :key="bible_books?.[0]?.id"
    >
      <MainTitle
        v-if="bible_books?.[0]?.part_ru"
        :title="bible_books[0].part_ru"
        textColor="red-darken-3"
        :hasDivider="true"
      />
      <TimelineBibleBooks :bible_books="bible_books" />
      <v-divider />
    </template>
  </div>
</template>

<script>


import TimelineBibleBooks from "@/components/book/timeline/TimelineBibleBooks.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import MainBigTitle from "@/components/common/title/MainBigTitle.vue";

export default {
  components: { MainBigTitle, MainTitle, TimelineBibleBooks },
  props: {
    bible_books: {
      type: Array,
      required: true
    }
  },
  computed: {
    sorted_bible_books() {
      return Object.values(this.bible_books).sort((bible_book_1, bible_book_2) => bible_book_1.id > bible_book_2.id ? 1 : -1);
    },
    evangelies() {
      return Object.values(this.sorted_bible_books).filter(bible_book => bible_book.part === "evangel");
    },
    apostols() {
      return Object.values(this.sorted_bible_books).filter(bible_book => bible_book.part === "apostle");
    },
    pjatiknizhieMoiseja() {
      return Object.values(this.sorted_bible_books).filter(bible_book => bible_book.part === "pjatiknizhie_moiseja");
    },
    psaltyr() {
      return Object.values(this.sorted_bible_books).filter(bible_book => bible_book.part === "psaltyr");
    },
    oldTestamentOtherBibleBooks() {
      return Object.values(this.sorted_bible_books).filter(bible_book => bible_book.testament === "old_testament" & !bible_book.part);
    }
  }
};
</script>
