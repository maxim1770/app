<template>
  <div
    v-if="sourceImageObjects.length"
    @click="previewImgObject"
    class="d-flex justify-center mt-1"
  >
    <ImgWithPlaceholder
      :src="has_preview_img ? sourceImageObjects[preview_img_num]['src'] : sourceImageObjects[preview_img_num]['data-source']"
      :has_cover="has_cover"
    />
  </div>
</template>
<script>
import "viewerjs/dist/viewer.css";
import { api as viewerApi } from "v-viewer";
import ImgWithPlaceholder from "@/components/gallery/ImgWithPlaceholder.vue";
import { imgUrl } from "@/utils/common";

export default {
  components: { ImgWithPlaceholder },
  props: {
    imgs_paths: {
      type: Array,
      required: true
    },
    preview_img_num: {
      type: Number,
      required: false,
      default: 0
    },
    has_preview_img: {
      type: Boolean,
      required: false,
      default: true
    },
    has_cover: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  computed: {
    sourceImageObjects() {
      const sourceImageObjects = [];
      for (const img_path of this.imgs_paths || []) {
        sourceImageObjects.push(
          {
            "src": imgUrl(img_path.replace("img\\", "preview-img\\")),
            "data-source": imgUrl(img_path)
          }
        );
      }
      return sourceImageObjects;
    }
  },
  methods: {
    previewImgObject() {
      const $viewer = viewerApi({
        options: {
          toolbar: true,
          button: true,
          transition: true,
          title: 3,
          url: "data-source",
          initialViewIndex: this.preview_img_num
        },
        images: this.sourceImageObjects
      });
    }
  }
};
</script>

