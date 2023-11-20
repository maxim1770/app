<template>
  <div>
    <ImgMainTitle
      mainPageValue="cathedrals"
      @click="$router.push({ name: 'cathedrals' })"
    />
    <CathedralsPage :cathedrals="cathedrals" />
    <CardRandomBook />
  </div>
</template>

<script>
import { api } from "@/services/api";
import CathedralsPage from "@/components/pages/CathedralsPage.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import CardRandomBook from "@/components/book/random_book/CardRandomBook.vue";

export default {
  components: { CardRandomBook, ImgMainTitle, CathedralsPage },

  data() {
    return {
      cathedrals: {
        type: Object,
        required: true
      }
    };
  },

  mounted() {
    api
      .getCathedrals()
      .then((response) => (this.cathedrals = response.data));
  }
};
</script>
