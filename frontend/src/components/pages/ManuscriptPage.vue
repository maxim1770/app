<template>
  <div class="d-flex flex-column align-content-center">
    <ImgWithPlaceholder :src="imgUrl(manuscript.manuscript?.preview_img_path)" />
    <h4 class="text-h4 font-weight-bold ma-2">
      <ManuscriptFullTitle :manuscript="manuscript.manuscript" />
    </h4>
    <v-divider></v-divider>
    <v-list lines="one">
      <v-list-item v-if="manuscript.manuscript?.fund" prepend-icon="mdi-bookshelf">
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
      <v-list-item v-else="manuscript.manuscript?.url" prepend-icon="mdi-bookshelf">
        <a>
          <v-chip
            variant="tonal"
            color="green"
          >
            Рукопись взята с сайта "Руниверс" {{ manuscript.manuscript?.url }}
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
    <!--      <a href="http://127.0.0.1:80/api/files/pdf/manuscripts\rsl\f_113\f-113-629.pdf">Скачать в формате PDF</a>-->
    <!--      <a href="manuscript.manuscript.pdf">Скачать в формате PDF (не работает)</a>-->
    <!--    </div>-->
    <!--    <v-divider></v-divider>-->

    <div
      v-if="hasBookmarks"
      class="mt-2"
    >
      <h3>Содержание:</h3>
      <ManuscriptContentFactory :manuscript="manuscript.manuscript" />
      <v-divider></v-divider>
    </div>
    <!--    <div-->
    <!--      v-if="manuscript.other_manuscripts?.length"-->
    <!--      class="mt-2"-->
    <!--    >-->
    <!--      <h3>Другие Рукописи:</h3>-->
    <!--      &lt;!&ndash;      <v-carousel show-arrows="hover">&ndash;&gt;-->
    <!--      &lt;!&ndash;        <v-carousel-item&ndash;&gt;-->
    <!--      &lt;!&ndash;          v-for="manuscript_near in manuscript.other_manuscripts"&ndash;&gt;-->
    <!--      &lt;!&ndash;          :key="manuscript_near.id"&ndash;&gt;-->
    <!--      &lt;!&ndash;          :to="{ name: 'manuscript', params: { manuscriptCode: manuscript_near.code } }"&ndash;&gt;-->
    <!--      &lt;!&ndash;          :src="imgUrl(manuscript_near.preview_img_path)"&ndash;&gt;-->
    <!--      &lt;!&ndash;          cover&ndash;&gt;-->
    <!--      &lt;!&ndash;        >&ndash;&gt;-->
    <!--      &lt;!&ndash;        </v-carousel-item>&ndash;&gt;-->
    <!--      &lt;!&ndash;      </v-carousel>&ndash;&gt;-->
    <!--      <div class="d-block d-lg-flex flex-wrap justify-center">-->
    <!--        <v-card-->
    <!--          v-for="manuscript_near in manuscript.other_manuscripts"-->
    <!--          :key="manuscript_near.id"-->
    <!--          :to="{ name: 'manuscript', params: { manuscriptCode: manuscript_near.code } }"-->
    <!--          max-width="500"-->
    <!--          max-height="1000"-->
    <!--          class="mx-1 my-1"-->
    <!--        >-->
    <!--          <v-img-->
    <!--            :src="imgUrl(manuscript_near.preview_img_path)"-->
    <!--            height="500px"-->
    <!--            width="1000px"-->
    <!--            cover-->
    <!--          ></v-img>-->
    <!--          <v-card-text>-->
    <!--            <ManuscriptFullTitle :manuscript="manuscript_near" />-->
    <!--          </v-card-text>-->
    <!--        </v-card>-->
    <!--        <v-divider></v-divider>-->
    <!--      </div>-->
    <!--    </div>-->

    <div
      class="mt-2"
    >
      <v-list>
        <v-list-item
          v-for="manuscript in this.manuscripts.items"
          :key="manuscript.id"
          :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
          prepend-icon="mdi-bookshelf"
          rounded="xl"
        >
          <ManuscriptFullTitle :manuscript="manuscript" />
        </v-list-item>
      </v-list>
    </div>
  </div>
</template>

<script>


import { imgUrl } from "@/utils/common";
import ImgWithPlaceholder from "@/components/common/ImgWithPlaceholder.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import ListItemYear from "@/components/year/ListItemYear.vue";
import RatingHandwriting from "@/components/manuscript/RatingHandwriting.vue";
import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import ManuscriptContentFactory from "@/components/manuscript/manuscript_content/ManuscriptContentFactory.vue";
import { api } from "@/services/api";

export default {
  components: {
    ManuscriptFullTitle, ManuscriptContentFactory,
    BookFullTitleFactory, ImgWithPlaceholder, ListItemYear, RatingHandwriting
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      manuscripts: {
        type: Object,
        required: true
      },
      page: 1
    };
  },
  computed: {
    hasBookmarks() {
      if (Array.isArray(this.manuscript.manuscript?.bookmarks_)) {
        if (this.manuscript.manuscript?.bookmarks_.length) {
          return true;
        } else {
          return false;
        }
      } else if (typeof this.manuscript.manuscript?.bookmarks_ === "object" || this.manuscript.manuscript?.bookmarks_ !== null) {
        return true;
      } else {
        return false;
      }
    }
  },
  watch: {
    "manuscripts.items": function(newVal, oldVal) {
      this.page += 1;
    }
  },
  beforeMount() {
    api.getManuscripts({ page: this.page }).then((response) => (this.manuscripts = response.data));
  },
  mounted() {
    this.scroll();
  },
  methods: {
    imgUrl,
    scroll() {
      window.onscroll = () => {
        let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          api.getManuscripts({ page: this.page }).then((response) => (this.manuscripts.items = this.manuscripts.items?.concat(response.data.items)));
        }
      };
    }
  }
};
</script>

