<template>
  <div>
    <h1 class="text-center text-red-darken-4 my-2 ">Библия</h1>
    <v-divider></v-divider>
    <div>
      <h2 class="text-center text-red-darken-4 my-2">Новый Завет</h2>
      <v-divider></v-divider>
      <template
        v-for="bible_books in [evangelies, apostols]"
        :key="bible_books?.[0]?.id"
      >
        <h2 class="text-center text-red-darken-3 my-2">{{ bible_books?.[0]?.part_ru }}</h2>
        <v-divider></v-divider>
        <TimelineBibleBooks :bible_books="bible_books" />
        <v-divider></v-divider>
      </template>
      <h2 class="text-center text-red-darken-4 my-2">Ветхий Завет</h2>
      <v-divider></v-divider>
      <template
        v-for="bible_books in [pjatiknizhieMoiseja, psaltyr, oldTestamentOtherBibleBooks]"
        :key="bible_books?.[0]?.id"
      >
        <template v-if="bible_books?.[0]?.part_ru">
          <h2 class="text-center text-red-darken-3 my-2">{{ bible_books[0].part_ru }}</h2>
          <v-divider></v-divider>
        </template>
        <TimelineBibleBooks :bible_books="bible_books" />
        <v-divider></v-divider>
      </template>
    </div>
  </div>
</template>

<script>


import TimelineBibleBooks from "@/components/book/timeline/TimelineBibleBooks.vue";

export default {
  components: { TimelineBibleBooks },
  props: {
    bible_books: {
      type: Object,
      required: true
    }
  },
  computed: {
    evangelies() {
      return Object.values(this.bible_books).filter(bible_book => bible_book.part === "evangel");
    },
    apostols() {
      return Object.values(this.bible_books).filter(bible_book => bible_book.part === "apostle");
    },
    pjatiknizhieMoiseja() {
      return Object.values(this.bible_books).filter(bible_book => bible_book.part === "pjatiknizhie_moiseja");
    },
    psaltyr() {
      return Object.values(this.bible_books).filter(bible_book => bible_book.part === "psaltyr");
    },
    oldTestamentOtherBibleBooks() {
      return Object.values(this.bible_books).filter(bible_book => bible_book.testament === "old_testament" & !bible_book.part);
    }
  }
};
</script>
