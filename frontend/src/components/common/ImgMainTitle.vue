<template>
  <ImgWithPlaceholder
    v-once
    :src="imgUrl(mainPage.img)"
    :style="{ 'height': xlAndUp ? '450px' : '250px'}"
    class="mb-5"
  >
    <MainBigTitle
      :title="title || mainPage.title"
      :textColor="textColor"
    />
  </ImgWithPlaceholder>
</template>

<script>
import ImgWithPlaceholder from "@/components/gallery/ImgWithPlaceholder.vue";
import { imgUrl, mainPages } from "@/utils/common";
import { useDisplay } from "vuetify";
import MainBigTitle from "@/components/common/title/MainBigTitle.vue";

export default {
  components: { MainBigTitle, ImgWithPlaceholder },
  props: {
    mainPageValue: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: false,
      default: null
    },
    textColor: {
      type: String,
      required: false,
      default: "white"
    }
  },
  computed: {
    mainPage() {
      return mainPages.find(mainPage => mainPage.value === this.mainPageValue);
    }
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  methods: { imgUrl }

};
</script>







