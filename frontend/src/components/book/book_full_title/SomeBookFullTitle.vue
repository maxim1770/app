<template>
  <v-chip
    v-if="isChapters"
    color="red"
  >
    Главы
  </v-chip>
  <v-chip
    v-else-if="hasQuestionMark"
    color="red"
    class="ma-1"
  >
    Закладка
  </v-chip>
  <v-chip
    v-else
    color="light-blue-accent-3"
    class="ma-1"
  >
    {{ book?.bookmark_title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    isChapters() {
      return this.book?.bookmark_title === "Содержание";
    },
    hasQuestionMark() {
      return this.book?.bookmark_title?.includes("?");
    }
  }
};

</script>



