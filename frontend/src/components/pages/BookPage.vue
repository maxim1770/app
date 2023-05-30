<template>
  <div>
    <div class="d-flex justify-center mb-5 mt-2 align-center">
      <v-btn
        color="blue"
        @click="$router.push({ name: 'book', params: { bookId: preBook } })"
        class="mr-12"
      >
        <v-icon icon="mdi-arrow-left"></v-icon>
      </v-btn>
      <p class="text-h2"> Выдержка</p>
      <v-btn
        color="blue"
        @click="$router.push({ name: 'book', params: { bookId: nextBook } })"
        class="ml-12"
      >
        <v-icon icon="mdi-arrow-right"></v-icon>
      </v-btn>
    </div>
    <v-divider></v-divider>
    <v-list lines="one">
      <v-list-item class="d-flex justify-center align-content-center">
        <v-chip-group>
          <CurrentBookFactory :book="book" />
        </v-chip-group>
      </v-list-item>
      <v-divider></v-divider>
      <ListItemManuscript :manuscript="book.manuscripts?.[0].manuscript" />
    </v-list>
    <v-divider></v-divider>

    <!--    {{ api.getAsset("img//manuscripts//rsl//f_218//f-218-1132//177.webp") }}-->
    <!--    <BlobImage src="http://localhost:80/assets/img//manuscripts//rsl//f_218//f-218-1132//177.webp"></BlobImage>-->


    <lightgallery
      :settings="{ speed: 500, plugins: plugins }"
      :onInit="onInit"
      :onBeforeSlide="onBeforeSlide"
    >
      <a
        v-for="img in book.manuscripts?.[0].imgs"
        :data-src="imgUrl(img)"
      >
        <img
          className="img-responsive"
          :src="imgUrl(img)"
        />
      </a>
    </lightgallery>
  </div>

</template>

<script>
import { api } from "@/services/api";
import Lightgallery from "lightgallery/vue";
import lgThumbnail from "lightgallery/plugins/thumbnail";
import lgZoom from "lightgallery/plugins/zoom";
import BlobImage from "@/components/BlobImage.vue";
import { imgUrl } from "@/utils/common";
import CurrentBookFactory from "@/components/book/CurrentBookFactory.vue";
import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";

let lightGallery = null;
export default {
  components: { ListItemManuscript, CurrentBookFactory, Lightgallery, BlobImage },

  props: {
    book: {
      type: Object,
      required: true
    }
  },
  data: () => ({
    plugins: [lgThumbnail, lgZoom]
  }),
  computed: {
    api() {
      return api;
    },
    preBook() {
      return this.book.id - 1;
    },
    nextBook() {
      return this.book.id + 1;
    }
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


<style lang="css">
@import 'lightgallery.css';
@import 'lg-thumbnail.css';
@import 'lg-zoom.css';
</style>



