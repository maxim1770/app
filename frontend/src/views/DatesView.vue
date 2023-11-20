<template>
  <div>
    <ImgMainTitle
      mainPageValue="dates"
      @click="$router.push({ name: 'dates' })"
    />
    <DatesPage />
  </div>
</template>

<script>
import DatesPage from "@/components/pages/DatesPage.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";

export default {
  components: { ImgMainTitle, DatesPage }
};
</script>










