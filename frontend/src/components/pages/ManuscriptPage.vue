<template>

  <div class="d-flex flex-column align-content-center">
    <ImgWithPlaceholder :src="imgUrl(manuscript.manuscript?.preview_img_path)" />
    <h4 class="text-h4 font-weight-bold ma-2">
      <ManuscriptFullTitle :manuscript="manuscript.manuscript" />
    </h4>
    <v-divider></v-divider>
    <v-list lines="one">
      <v-list-item prepend-icon="mdi-bookshelf">
        Шифр:
        <a class="ml-1">
          <v-chip
            variant="tonal"
            color="green"
          >
            {{ manuscript.manuscript?.fund.library }}
          </v-chip>
          <v-chip class="ml-1">
            {{ manuscript.manuscript?.code_title }}
          </v-chip>
        </a>
      </v-list-item>
      <v-list-item v-if="manuscript.manuscript?.neb_url" prepend-icon="mdi-bookshelf">
        <a>
          Рукопись на сайте библиотеки
          <v-chip
            variant="tonal"
            color="green"
            class="ml-1"
          >
            НЕБ
          </v-chip>
        </a>
        <v-divider class="mt-1"></v-divider>
      </v-list-item>
      <ListItemYear :year="manuscript.manuscript?.year" />
      <v-list-item prepend-icon="mdi-pencil-outline">
        Почерк:
        <RatingHandwriting :manuscript="manuscript?.manuscript" class="ml-1" />
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <!--    <div>-->
    <!--      <a href="http://127.0.0.1:80/files/pdf/manuscripts\rsl\f_113\f-113-629.pdf">Скачать в формате PDF</a>-->
    <!--      <a href="manuscript.manuscript.pdf">Скачать в формате PDF (не работает)</a>-->
    <!--    </div>-->
    <!--    <v-divider></v-divider>-->
    <div
      v-if="manuscript.manuscript?.books?.length"
      class="mt-2"
    >
      <h3>Содержание:</h3>
      <v-list lines="one">
        <v-list-item
          v-for="bookmark in manuscript.manuscript?.books"
          :key="bookmark?.id"
          :to="{ name: 'book', params: { bookId: bookmark.book?.id } }"
          rounded="lg"
        >
          <v-chip-group>
            <v-chip
              variant="text"
            >
              л. {{ bookmark.first_page?.num }}.
            </v-chip>
            <CurrentBookFactory :book="bookmark?.book" />
          </v-chip-group>
          <v-divider></v-divider>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
    </div>
    <div
      v-if="manuscript.manuscripts_near?.length"
      class="mt-2"
    >
      <h3>Другие Рукописи:</h3>
      <!--      <v-carousel show-arrows="hover">-->
      <!--        <v-carousel-item-->
      <!--          v-for="manuscript_near in manuscript.manuscripts_near"-->
      <!--          :key="manuscript_near.id"-->
      <!--          :to="{ name: 'manuscript', params: { manuscriptCode: manuscript_near.code } }"-->
      <!--          :src="imgUrl(manuscript_near.preview_img_path)"-->
      <!--          cover-->
      <!--        >-->
      <!--        </v-carousel-item>-->
      <!--      </v-carousel>-->
      <div class="d-block d-lg-flex flex-wrap justify-center">
        <v-card
          v-for="manuscript_near in manuscript.manuscripts_near"
          :key="manuscript_near.id"
          :to="{ name: 'manuscript', params: { manuscriptCode: manuscript_near.code } }"
          max-width="500"
          max-height="1000"
          class="mx-1 my-1"
        >
          <v-img
            :src="imgUrl(manuscript_near.preview_img_path)"
            height="500px"
            width="1000px"
            cover
          ></v-img>
          <v-card-text>
            <ManuscriptFullTitle :manuscript="manuscript_near" />
          </v-card-text>
        </v-card>
        <v-divider></v-divider>
      </div>
    </div>
  </div>
</template>

<script>


import { imgUrl } from "@/utils/common";
import ImgWithPlaceholder from "@/components/common/ImgWithPlaceholder.vue";
import CurrentBookFactory from "@/components/book/CurrentBookFactory.vue";
import ListItemYear from "@/components/year/ListItemYear.vue";
import RatingHandwriting from "@/components/manuscript/RatingHandwriting.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";


export default {
  components: {
    ManuscriptFullTitle,
    CurrentBookFactory, ImgWithPlaceholder, ListItemYear, RatingHandwriting
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  methods: {
    imgUrl
  }
};
</script>

