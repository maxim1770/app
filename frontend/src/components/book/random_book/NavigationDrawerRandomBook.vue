<template>
  <v-list>
    <v-list-item
      @click="getRandomBookId"
      class="text-center"
    >
      <v-badge
        content="Случайное"
        color="blue"
      />
      Слово, Поучение
    </v-list-item>
  </v-list>
</template>

<script>

import { api } from "@/services/api";

export default {

  data() {
    return {
      book_id: {
        type: Number
      }
    };
  },
  watch: {
    book_id() {
      this.$router.push({ name: "book", params: { bookId: this.book_id } });
    }
  },
  methods: {
    getRandomBookId() {
      api.getRandomBookId()
        .then((response) => (this.book_id = response.data.book_id));
    }
  }
};

</script>


