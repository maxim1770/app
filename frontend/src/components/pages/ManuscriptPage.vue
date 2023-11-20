<template>
  <div>
    <GalleryMain
      :imgs_paths="manuscript?.all_pages_paths"
      :preview_img_num="manuscript?.preview_page_num ? manuscript.preview_page_num : 0"
      :has_preview_img="false"
    />
    <MainTitle :title="manuscript?.title" />
    <!--    <AdminPutManuscriptData :manuscript="manuscript" />-->
    <ManuscriptData :manuscript="manuscript" />
    <ManuscriptContentFactory v-if="hasBookmarks" :manuscript="manuscript" />
  </div>
</template>

<script>


import { imgUrl } from "@/utils/common";
import ManuscriptContentFactory from "@/components/manuscript/manuscript_content/ManuscriptContentFactory.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import ManuscriptData from "@/components/manuscript/ManuscriptData.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";

export default {
  components: {
    ChapterWithHead,
    GalleryMain,
    ManuscriptData,
    MainTitle,
    ManuscriptContentFactory
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    hasBookmarks() {
      if (Array.isArray(this.manuscript?.structured_bookmarks)) {
        if (this.manuscript?.structured_bookmarks.length) {
          return true;
        } else {
          return false;
        }
      } else if (typeof this.manuscript?.structured_bookmarks === "object" || this.manuscript?.structured_bookmarks !== null) {
        return true;
      } else {
        return false;
      }
    }
  },
  methods: {
    imgUrl
  }
};
</script>

