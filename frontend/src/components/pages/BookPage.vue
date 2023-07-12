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
      <v-list-item class="text-center">
        <BookFullTitleFactory :book="book.book" />
      </v-list-item>
      <v-divider></v-divider>
      <ListItemManuscript :manuscript="bookmarkWithBestManuscriptHandwriting?.manuscript" />
    </v-list>
    <v-divider></v-divider>
    <!--    {{ api.getAsset("img//manuscripts//rsl//f_218//f-218-1132//177.webp") }}-->
    <!--    <BlobImage src="http://localhost:80/api/assets/img//manuscripts//rsl//f_218//f-218-1132//177.webp"></BlobImage>-->

    <!--    <lightgalleryBase :imgs="bookmarkWithBestManuscriptHandwriting?.imgs_paths" />-->


    <!--    <lightgalleryPro :imgs="bookmarkWithBestManuscriptHandwriting?.imgs_paths" />-->

    <!--    <VueGalleryBase :imgs="bookmarkWithBestManuscriptHandwriting?.imgs_paths" />-->

    <!--    <VViewerBase :imgs="bookmarkWithBestManuscriptHandwriting?.imgs_paths" />-->


    <div>
      <table>
        <thead>
        <tr>
          <th>Id</th>
          <th>Image</th>
        </tr>
        </thead>
        <tbody>
        <tr v-for="(image, index) in allImages" :key="index">
          <td>{{ index }}</td>
          <td>
            <button type="button" @click="show(index)">Click to show</button>
          </td>
        </tr>
        </tbody>
      </table>
      <img-viewer ref="viewer" />
    </div>


    <div
      v-if="book.book_tolkovoe"
      class="mt-2"
    >
      <h3>Толкование:</h3>
      <v-list lines="one">
        <v-list-item
          :to="{ name: 'book', params: { bookId: book.book_tolkovoe.id } }"
          rounded="xl"
          class="text-center"
        >
          <BookFullTitleFactory :book="book.book_tolkovoe" />
        </v-list-item>
        <v-divider></v-divider>
        <ListItemManuscript :manuscript="book.book_tolkovoe.bookmarks?.[0].manuscript" />
      </v-list>
      <v-divider></v-divider>
    </div>
    <div
      v-if="otherBookmarks.length"
      class="mt-2"
    >
      <h3>Читать в других Рукописях:</h3>
      <v-list>
        <v-list-item
          v-for="bookmark in otherBookmarks"
          :key="bookmark.manuscript.id"
          :to="{ name: 'manuscript', params: { manuscriptCode: bookmark.manuscript.code } }"
          rounded="xl"
        >
          <ChipBookmarkFirstPageNum :first_page="bookmark.first_page" class="mr-1" />
          <ManuscriptFullTitle :manuscript="bookmark.manuscript" />
        </v-list-item>
      </v-list>
    </div>
  </div>

</template>

<script>
import BlobImage from "@/components/BlobImage.vue";
import { imgUrl } from "@/utils/common";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import lightgalleryBase from "@/components/lightgallery/lightgalleryBase.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import ChipBookmarkFirstPageNum from "@/components/manuscript/ChipBookmarkFirstPageNum.vue";
import lightgalleryPro from "@/components/lightgallery/lightgalleryPro.vue";
import VueGalleryBase from "@/components/lightgallery/VueGalleryBase.vue";
import VViewerBase from "@/components/lightgallery/VViewerBase.vue";
import VViewerOther from "@/components/lightgallery/VViewerOther.vue";

export default {
  components: {
    VViewerOther,
    VViewerBase,
    VueGalleryBase,
    ManuscriptFullTitle,
    lightgalleryBase,
    lightgalleryPro,
    ListItemManuscript,
    BookFullTitleFactory,
    BlobImage,
    ChipBookmarkFirstPageNum
  },

  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    imgsWithHost() {
      const imgsWithHost_ = [];
      for (let i = 0; i < this.bookmarkWithBestManuscriptHandwriting?.imgs_paths?.length; i++) {
        imgsWithHost_.push(
          "http://localhost:81/assets/img//manuscripts//lls//lls-book-rus-1//40.webp"
        );
      }
      return imgsWithHost_;
    },
    preBook() {
      return this.book.book.id - 1;
    },
    nextBook() {
      return this.book.book.id + 1;
    },
    bookmarkWithBestManuscriptHandwriting() {
      return Object.assign([], this.book.book?.bookmarks).sort((b1, b2) => b1.manuscript?.handwriting > b2.manuscript?.handwriting ? 1 : -1)[0];
    },
    otherBookmarks() {
      return Object.assign([], this.book.book?.bookmarks).sort((b1, b2) => b1.manuscript?.handwriting > b2.manuscript?.handwriting ? 1 : -1).slice(1);
    }
  },
  methods: {
    imgUrl,
    show(index) {
      this.$refs.viewer.show(
        this.imgsWithHost[index],
        Math.floor(Math.random() * 10)
      );
    }
  }
};
</script>








