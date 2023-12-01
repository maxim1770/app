<template>
  <div>
    <MovableDatesPage
      v-if="movableDates[0]"
      :movableDates="movableDates"
    />
    <CardRandomBook />
  </div>
</template>

<script>
import { api } from "@/services/api";
import MovableDatesPage from "@/components/pages/MovableDatesPage.vue";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";

export default {
  components: { MovableDatesPage, CardRandomBook },

  data() {
    return {
      movableDates: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getMovableDates()
      .then((response) => (this.movableDates = response.data));
  }
};
</script>
