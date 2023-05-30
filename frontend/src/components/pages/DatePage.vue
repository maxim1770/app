<template>
  <div class="75">
    <div class="d-flex justify-center mb-5 mt-2 align-center">
      <v-btn
        color="blue"
        @click="$router.push({ name: 'date', params: { date: preDate } })"
        class="mr-12"
      >
        <v-icon icon="mdi-arrow-left"></v-icon>
      </v-btn>
      <p class="text-h2">{{ date.day?.title }}</p>
      <v-btn
        color="blue"
        @click="$router.push({ name: 'date', params: { date: nextDate } })"
        class="ml-12"
      >
        <v-icon icon="mdi-arrow-right"></v-icon>
      </v-btn>
    </div>
    <v-divider></v-divider>
    <v-list v-if="date.day?.holidays.length">
      <v-list-item
        v-for="holiday in date.day.holidays"
        :key="holiday.id"
        :to="{ name: 'holiday', params: { holidaySlug: holiday.slug } }"
        rounded="xl"
        class="mb-1"
        :class="{
          'bg-red-accent-4': isGreatHoliday(holiday.holiday_category?.title)
        }"
      >
        {{ holiday.title }}
        <ChipYear v-if="holiday.year" :year="holiday.year" class="ml-1" />
        <ChipHolidayCategory :holiday_category="holiday.holiday_category" class="ml-1" />
      </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <div
      v-if="date.movable_day?.movable_date_books?.length"
      class="mt-2"
    >
      <h3>Поучения по времени:</h3>
      <div
        v-for="movable_date_book in date.movable_day?.movable_date_books"
        :key="movable_date_book.id"
      >
        <p>{{ movable_date_book?.type }}</p>
        <!--          <lightgallery-->
        <!--            :settings="{ speed: 500, plugins: plugins }"-->
        <!--            :onInit="onInit"-->
        <!--            :onBeforeSlide="onBeforeSlide"-->
        <!--          >-->
        <!--            <a-->
        <!--              v-for="img in movable_date_book.book.manuscripts?.[0].imgs"-->
        <!--              :data-src="img"-->
        <!--              className="gallery-item"-->
        <!--            >-->
        <!--              <img-->
        <!--                className="img-responsive"-->
        <!--                :src="img"-->
        <!--              />-->
        <!--            </a>-->
        <!--          </lightgallery>-->
      </div>
    </div>
    <v-divider></v-divider>
  </div>
</template>

<script>

// import lgThumbnail from "lightgallery/plugins/thumbnail";
// import lgZoom from "lightgallery/plugins/zoom";
// import Lightgallery from "lightgallery/vue";
import { nextDate, preDate } from "@/utils/date";
import ChipYear from "@/components/year/ChipYear.vue";
import { isGreatHoliday } from "@/utils/holidays";
import ChipHolidayCategory from "@/components/holiday/ChipHolidayCategory.vue";

// let lightGallery = null;

export default {
  components: { ChipYear, ChipHolidayCategory },
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      // plugins: [lgThumbnail, lgZoom]
    };
  },
  computed: {
    preDate() {
      return preDate(this.date.day?.month_day);
    },
    nextDate() {
      return nextDate(this.date.day?.month_day);
    }
  },
  methods: {
    isGreatHoliday
    //   onInit: (detail) => {
    //     lightGallery = detail.instance;
    //   },
    //   onBeforeSlide: () => {
    //     console.log("calling before slide");
    //   }
    // }
  }
};
</script>


<!--<style lang="css">-->
<!--@import 'lightgallery.css';-->
<!--@import 'lg-thumbnail.css';-->
<!--@import 'lg-zoom.css';-->

<!--.gallery-item {-->
<!--  margin: 5px-->
<!--}-->
<!--</style>-->