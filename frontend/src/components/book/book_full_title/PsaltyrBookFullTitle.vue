<template>
  <v-chip
    v-if="book && book.title.includes('толк')"
    :to="{ name: 'book', params: { bookId: book.id } }"
    prepend-icon="mdi-check-circle-outline"
    color="blue"
    class="ma-1"
  >
    Толковый
  </v-chip>
  <ChipZachalo
    :zachalo="book.psaltyr_book"
    :hasBibleBookLink="true"
    :isPsaltyrBook="true"
    :hasAlwaysSeeOptional="true"
  />
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";
import ChipZachalo from "@/components/book/ChipZachalo.vue";

export default {
  components: { ChipZachalo, BadgeNum },
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>

