<template>
  <div>
    <ImgMainTitle mainPageValue="lls" />
    <div>
      <v-divider />
      <MainTitle title="Библейская история" textColor="red-darken-3" :hasDivider="true" />
      <TimelineLls :llsManuscripts="llsBibleManuscripts" />
      <v-divider />
      <MainTitle title="Всемирная история" textColor="red-darken-3" :hasDivider="true" />
      <TimelineLls :llsManuscripts="llsOtherManuscripts" />
      <v-divider />
      <MainTitle title="Русская летописная история" textColor="red-darken-3" :hasDivider="true" />
      <TimelineLls :llsManuscripts="llsRusManuscripts" />
      <v-divider />
    </div>
  </div>
</template>

<script>


import TimelineLls from "@/components/book/timeline/TimelineLls.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import MainBigTitle from "@/components/common/title/MainBigTitle.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";

export default {
  components: { ImgMainTitle, MainBigTitle, MainTitle, TimelineLls },
  props: {
    llsManuscripts: {
      type: Object,
      required: true
    }
  },
  computed: {
    llsBibleManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => manuscript.title?.includes("Библейская история"));
    },
    llsOtherManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => !manuscript.title?.includes("Библейская история") & !manuscript.code?.includes("rus"));
    },
    llsRusManuscripts() {
      return Object.values(this.llsManuscripts).filter(manuscript => manuscript.code?.includes("rus"));
    }
  }

};
</script>
