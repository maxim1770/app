<template>
  <Carousel id="gallery" :items-to-show="1" :wrap-around="false" v-model="currentSlide">
    <Slide v-for="img_data in imgs_data" :key="img_data.id">
      <div class="carousel__item">
        <img :src="imgUrl(img_data.path.replace('img\\', 'preview-img\\'))" :alt="img_data.desc" />
      </div>
    </Slide>
  </Carousel>

  <Carousel
    id="thumbnails"
    :items-to-show="4"
    :wrap-around="true"
    v-model="currentSlide"
    ref="carousel"
  >
    <Slide v-for="img_data in imgs_data" :key="img_data.id">
      <div class="carousel__item" @click="slideTo(slide - 1)">
        <img :src="imgUrl(img_data.path.replace('img\\', 'preview-img\\'))" :alt="img_data.desc" />
      </div>
    </Slide>
  </Carousel>
</template>

<script>
import { defineComponent } from "vue";
import { Carousel, Navigation, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";
import { imgUrl } from "@/utils/common";

export default defineComponent({
  name: "Gallery",
  components: {
    Carousel,
    Slide,
    Navigation
  },
  props: {
    imgs_data: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      currentSlide: 0
    };
  },
  methods: {
    imgUrl,
    slideTo(val) {
      this.currentSlide = val;
    }
  }
});
</script>