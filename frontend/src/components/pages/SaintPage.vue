<template>
  <h4 class="text-h4 font-weight-bold">
    {{ saint.name }}
    <ChipFaceSanctity v-if="saint.face_sanctity" :face_sanctity="saint.face_sanctity" class="ml-1" />
    <ChipDignity v-if="saint.dignity" :dignity="saint.dignity" class="ml-1" />
  </h4>

  <!--   </hr>-->
  "Дни памяти"

  <v-list lines="one">
    <v-list-item
      v-for="holiday in saint.holidays"
      :key="holiday.id"
      :title="holiday.title"
      :to="{ name: 'holiday', params: { holidaySlug: holiday.slug } }"
    >
    </v-list-item>
  </v-list>

  <!--  <div>-->
  <!--    <h1>Труд:</h1>-->
  <!--    <div-->
  <!--        v-for="book in holiday.books"-->
  <!--        :key="book.id"-->
  <!--    >-->
  <!--      <lightgallery-->
  <!--          :settings="{ speed: 500, plugins: plugins }"-->
  <!--          :onInit="onInit"-->
  <!--          :onBeforeSlide="onBeforeSlide"-->
  <!--      >-->
  <!--        <a-->
  <!--            v-for="img in book.manuscripts?.[0].imgs"-->
  <!--            :data-src="img"-->
  <!--            :data-sub-html="book.title"-->
  <!--            className="gallery-item"-->
  <!--        >-->
  <!--          <img-->
  <!--              className="img-responsive"-->
  <!--              :src="img"-->
  <!--          />-->
  <!--        </a>-->
  <!--      </lightgallery>-->
  <!--    </div>-->
  <!--  </div>-->


</template>

<script>
import Lightgallery from "lightgallery/vue";
import lgThumbnail from "lightgallery/plugins/thumbnail";
import lgZoom from "lightgallery/plugins/zoom";
import ChipDignity from "@/components/saint/ChipDignity.vue";
import ChipFaceSanctity from "@/components/saint/ChipFaceSanctity.vue";

// If you are using scss you can skip the css imports below and use scss instead

export default {
  components: {
    ChipFaceSanctity, ChipDignity,
    Lightgallery
  },
  props: {
    saint: {
      type: Object,
      required: true
    }
  },
  data: () => ({
    plugins: [lgThumbnail, lgZoom]
  }),
  methods: {
    onInit: () => {
      console.log("lightGallery has been initialized");
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
