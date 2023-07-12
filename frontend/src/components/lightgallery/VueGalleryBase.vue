<template>
  <div>
    <gallery :images="imgsWithHost" :index="index" @close="index = null"></gallery>
    <div
      class="image"
      v-for="(image, imageIndex) in imgsWithHost"
      :key="imageIndex"
      @click="index = imageIndex"
      :style="{ backgroundImage: 'url(' + image + ')', width: '300px', height: '200px' }"
    ></div>
  </div>

  <div>
    <gallery :images="imgsWithHost" :thumbnails="true" :slide-delay="5000" :lightbox-options="{wrapAround: true}"
             :current-image="0" />
  </div>

</template>

<script>

import VueGallery from "vue-gallery";


export default {
  components: { "gallery": VueGallery },
  props: {
    imgs: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      index: null
    };
  },
  computed: {
    imgsWithHost() {
      const imgsWithHost_ = [];
      for (let i = 0; i < this.imgs?.length; i++) {
        imgsWithHost_.push(
          "http://localhost:81/assets/img//manuscripts//lls//lls-book-rus-1//40.webp"
        );
      }
      return imgsWithHost_;
    }
  }
};
</script>


<style scoped>
.image {
  float: left;
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  border: 1px solid #ebebeb;
  margin: 5px;
}
</style>