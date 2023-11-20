<template>
  <ChipYear
    v-if="book.lls_book.has_year_at_start"
    :year="book.lls_book.year"
    :title="llsYearTitle"
    class="ma-1"
  />
  <span
    v-if="book.bookmark_title"
    class="text-body-1 ma-1"
  >
    {{ book.bookmark_title }}
  </span>
  <ChipYear
    v-if="!book.lls_book.has_year_at_start"
    :year="book.lls_book.year"
    :title="llsYearTitle"
    class="ma-1"
  />
  <v-chip
    v-if="!book.lls_book.is_chapter"
    color="red-lighten-2"
    prepend-icon="mdi-alert-circle-outline"
    class="ma-1"
  >
    Не выделено в Рукописи
  </v-chip>
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";

export default {
  components: { ChipYear },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    llsYearTitle() {
      return "В лето";
    }
  }
};

</script>



