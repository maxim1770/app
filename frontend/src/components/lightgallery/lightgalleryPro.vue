<template>
  <div ref="galleryContainer" style="width: 500px; height: 1000px"></div>
  <div v-if="galleryContainer && imgsWithHost?.length">
    <lightgallery
      :settings="{ speed: 500, closable: false, container:galleryContainer,  plugins: plugins, dynamic: true, dynamicEl:imgsWithHost }"
      :onInit="onInit"
      :onBeforeSlide="onBeforeSlide"
    >
      <!--      <a-->
      <!--        v-for="img in imgs"-->
      <!--        :key="img"-->
      <!--        :data-src="imgUrl(img)"-->
      <!--        className="gallery-item"-->
      <!--      >-->
      <!--        <img-->
      <!--          className="img-responsive"-->
      <!--          :src="imgUrl(img)"-->
      <!--        />-->
      <!--      </a>-->
    </lightgallery>
  </div>
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
      plugins: [lgThumbnail, lgZoom],
      galleryContainer: this.$refs.galleryContainer
    };
  },
  computed: {
    imgsWithHost() {
      const imgsWithHost_ = [];
      for (let i = 0; i < this.imgs.length; i++) {
        imgsWithHost_.push(
          {
            "src": imgUrl(this.imgs[i].src),
            "thumb": imgUrl(this.imgs[i].src)
          }
        );
      }
      return imgsWithHost_;
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.galleryContainer = this.$refs.galleryContainer;
    });
  },
  methods: {
    imgUrl,
    onInit: (detail) => {
      lightGallery = detail.instance;
      detail.instance.openGallery(0);
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



