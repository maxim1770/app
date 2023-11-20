<template>
  <Carousel
    v-if="imgs_data?.length > 1"
    v-bind="settings"
    :breakpoints="breakpoints"
    :autoplay="3000"
    :pauseAutoplayOnHover="true"
    :wrapAround="true"
  >
    <Slide v-for="img_data in imgs_data" :key="img_data.icon.id">
      <div class="carousel__item">
        <router-link
          :to="{ name: 'icon', params: { iconId: img_data.icon.id } }"
        >
          <ImgWithPlaceholder
            :src="imgUrl(img_data.icon.path.replace('img\\', 'preview-img\\'))"
            :has_cover="has_cover"
          />
        </router-link>
      </div>
    </Slide>
    <template #addons="{ slidesCount }">
      <Pagination v-if="slidesCount > 1" />
      <Navigation v-if="slidesCount > 1" />
    </template>
  </Carousel>
  <router-link
    v-else-if="imgs_data?.[0]?.icon.id"
    :to="{ name: 'icon', params: { iconId: imgs_data[0].icon.id } }"
  >
    <ImgWithPlaceholder
      :src="imgUrl(imgs_data[0].icon.path.replace('img\\', 'preview-img\\'))"
      :has_cover="has_cover"
    />
  </router-link>
</template>

<script>
import { Carousel, Navigation, Pagination, Slide } from "vue3-carousel";

import "vue3-carousel/dist/carousel.css";
import { imgUrl } from "@/utils/common";
import ImgWithPlaceholder from "@/components/gallery/ImgWithPlaceholder.vue";

export default {

  components: {
    ImgWithPlaceholder,
    Pagination,
    Carousel,
    Slide,
    Navigation
  },
  props: {
    imgs_data: {
      type: Array,
      required: true
    },
    has_cover: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  data() {
    return {
      settings: {
        itemsToShow: 1,
        snapAlign: "center"
      },
      breakpoints: {
        1024: {
          itemsToShow: 2,
          snapAlign: "start"
        }
      }
    };
  },
  methods: { imgUrl }
};
</script>

<style lang="css">

.carousel__item {
  width: 100%;
  max-height: 450px;
}

.carousel__slide {
  padding: 3px;
}

</style>
