<template>
  <div>
    <LlsPage :llsManuscripts="llsManuscripts" />
    <CardRandomBook />
  </div>
</template>

<script>
import { api } from "@/services/api";
import LlsPage from "@/components/pages/LlsPage.vue";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";

export default {
  components: { CardRandomBook, LlsPage },

  data() {
    return {
      llsManuscripts: {
        type: Object,
        required: true
      }
    };
  },

  mounted() {
    api
      .getLls()
      .then((response) => (this.llsManuscripts = response.data));
  }
};
</script>
