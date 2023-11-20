<template>
  <div>
    <ImgMainTitle
      mainPageValue="saints"
      @click="$router.push({ name: 'saints' })"
    />
    <SaintsPage :saintsSearchData="saintsSearchData" />
  </div>
</template>

<script>
import SaintsPage from "@/components/pages/SaintsPage.vue";
import { api } from "@/services/api";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";

export default {
  components: { ImgMainTitle, SaintsPage },
  data() {
    return {
      saintsSearchData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getSaintsSearchData()
      .then((response) => (this.saintsSearchData = response.data));
  }
};


</script>


