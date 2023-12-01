<template>
  <v-chip-group class="d-flex justify-center">
    <v-chip
      v-for="some_book in some_books"
      :key="some_book.id"
      :to="{ name: 'book', params: { bookId: some_book.id } }"
      color="red-darken-2"
      class="bg-red-darken-2"
    >
      {{ some_book.num || some_book.rule_num }}
    </v-chip>
  </v-chip-group>
</template>

<script>


export default {
  props: {
    some_books: {
      type: Array,
      required: true
    }
  }
};
</script>
