<template>
  <ChipYear v-if="book.lls_book.year" :year="book.lls_book.year" class="mr-1" />
  <v-chip>
    {{ book.bookmark_title }}
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
  }
};

</script>



