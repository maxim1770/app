<template>
  <v-list>
    <v-list-item
      @click="getRandomBookId"
    >
      <template v-slot:prepend>
        <v-badge
          content="Случайное"
          class="mr-1"
          color="blue"
        />
      </template>
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


