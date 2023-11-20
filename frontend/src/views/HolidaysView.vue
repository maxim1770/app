<template>
  <div>
    <ImgMainTitle
      mainPageValue="holidays"
      @click="$router.push({ name: 'holidays' })"
    />
    <HolidaysPage :holidaysSearchData="holidaysSearchData" />
  </div>
</template>

<script>
import HolidaysPage from "@/components/pages/HolidaysPage.vue";
import { api } from "@/services/api";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";

export default {
  components: { ImgMainTitle, HolidaysPage },
  data() {
    return {
      holidaysSearchData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getHolidaysSearchData()
      .then((response) => (this.holidaysSearchData = response.data));
  }
};
</script>






