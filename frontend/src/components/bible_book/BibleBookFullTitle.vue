<template>
  <v-chip
    :to="{ name: 'bible-book', params: { bibleBookAbbr: bibleBook.abbr } }"
    :style="{ 'font-size': smAndDown ? 'xx-small' : 'larger' }"
    color="blue"
    class="ma-1"
  >
    {{ bibleBook.title }}
  </v-chip>
</template>

<script>


import { useDisplay } from "vuetify";

export default {
  props: {
    bible_book: {
      type: Object,
      required: false,
      default: null
    },
    book: {
      type: Object,
      required: false,
      default: null
    }
  },
  computed: {
    bibleBook() {
      return this.bible_book || this.__zachalo_or_psaltyr_book.bible_book;
    },
    __zachalo_or_psaltyr_book() {
      return this.book.zachalo || this.book.psaltyr_book;
    }
  },
  setup() {
    const smAndDown = useDisplay();
    return smAndDown;
  }
};

</script>
