<template>
  <lightgallery
    :settings="{ speed: 500, plugins: plugins }"
    :onInit="onInit"
    :onBeforeSlide="onBeforeSlide"
  >
    <a
      v-for="img in imgs"
      :key="img"
      :data-src="imgUrl(img)"
      className="gallery-item"
    >
      <img
        className="img-responsive"
        :src="imgUrl(img)"
      />
    </a>
  </lightgallery>
</template>

<script>

import Lightgallery from "lightgallery/vue";
import lgThumbnail from "lightgallery/plugins/thumbnail";
import lgZoom from "lightgallery/plugins/zoom";
import { imgUrl } from "@/utils/common";


let lightGallery = null;

export default {
  components: { Lightgallery },
  props: {
    imgs: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      plugins: [lgThumbnail, lgZoom]
    };
  },
  methods: {
    imgUrl,
    onInit: (detail) => {
      lightGallery = detail.instance;
    },
    onBeforeSlide: () => {
      console.log("calling before slide");
    }
  }
};
</script>


<style lang="css" scoped>
@import 'lightgallery/css/lightgallery.css';
@import 'lightgallery/css/lg-thumbnail.css';
@import 'lightgallery/css/lg-zoom.css';

.gallery-item {
  margin: 5px
}
</style>



