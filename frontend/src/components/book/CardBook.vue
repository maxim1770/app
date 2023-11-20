<template>
  <v-card>
    <GalleryMain :imgs_paths="bookmark?.pages_paths" />
    <v-card-item>
      <BookData
        :book="book"
        :bookmark="bookmark"
      />
    </v-card-item>
  </v-card>
</template>

<script>


import BookData from "@/components/book/BookData.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";

export default {
  components: { GalleryMain, BookData },
  props: {
    book: {
      type: Object,
      required: true
    },
    bookmark: {
      type: Object,
      required: true
    }
  }
};

</script>



