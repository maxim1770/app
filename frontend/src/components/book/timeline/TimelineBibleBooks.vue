<template>
  <v-timeline
    :side="lgAndDown ? 'end' : undefined"
    align="start"
  >
    <v-timeline-item
      v-for="bible_book in bible_books"
      :key="bible_book.id"
      dot-color="red-lighten-1"
      icon="mdi-book-open-page-variant"
      size="small"
      fill-dot
    >
      <BibleBookFullTitleByBibleBook
        :bible_book="bible_book"
        class="d-flex justify-center"
      />
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import { useDisplay } from "vuetify";
import BibleBookFullTitleByBibleBook from "@/components/bible_book/BibleBookFullTitle.vue";

export default {
  components: { BibleBookFullTitleByBibleBook },
  props: {
    bible_books: {
      type: Array,
      required: true
    }
  },
  setup() {
    const { smAndDown, lgAndDown } = useDisplay();
    return { smAndDown, lgAndDown };
  }
};

</script>



