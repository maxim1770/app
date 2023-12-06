<template>
  <div>
    <ImgMainTitle
      mainPageValue="manuscripts"
      @click="$router.push({ name: 'manuscripts' })"
    />
    <ManuscriptsPage :manuscriptsSearchData="manuscriptsSearchData" />
  </div>
</template>

<script>
import ManuscriptsPage from "@/components/pages/ManuscriptsPage.vue";
import { api } from "@/services/api";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";

export default {
  metaInfo() {
    return {
      title: "Рукописи",
      meta: [
        { vmid: "description", name: "description", content: "Рукописи до 1597 года" }
      ]
    };
  },
  components: { ImgMainTitle, ManuscriptsPage },
  data() {
    return {
      manuscriptsSearchData: {
        type: Object,
        required: true
      }
    };
  },
  mounted() {
    api
      .getManuscriptsSearchData()
      .then((response) => (this.manuscriptsSearchData = response.data));
  }
};
</script>




