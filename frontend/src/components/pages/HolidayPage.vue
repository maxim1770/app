<template>
  <div class="d-flex flex-column align-content-center">
    <lightgallery
      :settings="{ speed: 500, plugins: plugins }"
      :onInit="onInit"
      :onBeforeSlide="onBeforeSlide"
    >
      <a
        v-for="icon in holiday?.icons"
        :key="icon.id"
        :data-src="imgUrl(icon.path)"
        :data-sub-html="icon.desc"
      >
        <img
          className="img-responsive"
          :src="imgUrl(icon.path)"
          :to="{ name: 'icon', params: { iconSlug: icon.slug } }"
        />
      </a>
    </lightgallery>
    <h4 class="text-h4 font-weight-bold ma-2">
      {{ holiday.title }}
      <ChipHolidayCategory
        :holiday_category="holiday.holiday_category"
        class="ml-1"
        :class="{
      'text-red-darken-3': isGreatHoliday,
      'text-green': !isGreatHoliday
      }"
      />
    </h4>
    <v-divider></v-divider>
    <div>
      <v-list lines="one">
        <v-list-item
          v-if="holiday.day"
          prepend-icon="mdi-calendar-range"
        >
          День Памяти:
          <ChipDay :day="holiday.day" class="ml-1" />
        </v-list-item>
        <ListItemYear :year="holiday.year" />
      </v-list>
    </div>
    <v-divider></v-divider>
    <component
      :is="CurrentHolidayCategory"
      v-if="holiday.saints?.length"
      :holiday="holiday"
    />
    <v-divider></v-divider>
    <div
      v-if="holiday.holiday_books?.length"
      class="mt-2"
    >
      <h3>Жития, Прологи:</h3>
      <div
        v-for="holiday_book in holiday.holiday_books"
        :key="holiday_book.id"
      >
        <v-list lines="one">
          <v-list-item
            v-if="holiday_book?.book_util"
            prepend-icon="mdi-alert-outline"
          >
            <v-chip variant="tonal" color="red">
              Только упоминание
            </v-chip>
          </v-list-item>
          <ListItemManuscript :manuscript="holiday_book.book.manuscripts?.[0].manuscript" />
        </v-list>

        <!--        <div ref="galleryContainer" style="width: 1000px; height: 1500px"></div>-->
        <!--        <div v-if="galleryContainer && holiday_book.book.manuscripts?.[0].imgs.length">-->
        <!--          <lightgallery-->
        <!--            :settings="{ speed: 500, plugins: plugins, closable: false, container:galleryContainer, dynamic: true}"-->
        <!--            :onInit="onInit"-->
        <!--            :onBeforeSlide="onBeforeSlide"-->
        <!--          >-->
        <!--            <a-->
        <!--              v-for="img in holiday_book.book.manuscripts?.[0].imgs"-->
        <!--              :data-src="imgUrl(img)"-->
        <!--              className="gallery-item"-->
        <!--            >-->
        <!--              <img-->
        <!--                className="img-responsive"-->
        <!--                :src="imgUrl(img)"-->
        <!--              />-->
        <!--            </a>-->
        <!--          </lightgallery>-->
        <!--        </div>-->

        <v-divider inset></v-divider>
      </div>
    </div>
    <div
      v-if="holiday.molitva_books?.length"
      class="mt-2"
    >
      <h3>Тропари, кондаки:</h3>
      <div
        v-for="molitva_book in holiday.molitva_books"
        :key="molitva_book.id"
      >
        <v-list lines="one">
          <v-list-item
            prepend-icon="mdi-book-open-variant"
          >
            Название:
            <v-chip class="ml-1">
              {{ molitva_book.title }}
            </v-chip>
          </v-list-item>
          <ListItemManuscript :manuscript="molitva_book.book.manuscripts?.[0].manuscript" />
        </v-list>
        <!--        <lightgallery-->
        <!--          :settings="{ speed: 500, plugins: plugins }"-->
        <!--          :onInit="onInit"-->
        <!--          :onBeforeSlide="onBeforeSlide"-->
        <!--        >-->
        <!--          <a-->
        <!--            v-for="img in molitva_book.book.manuscripts?.[0].imgs"-->
        <!--            :data-src="imgUrl(img)"-->
        <!--            :data-sub-html="molitva_book.title"-->
        <!--          >-->
        <!--            <img-->
        <!--              className="img-responsive"-->
        <!--              :src="imgUrl(img)"-->
        <!--            />-->
        <!--          </a>-->
        <!--        </lightgallery>-->
        <v-divider inset></v-divider>
      </div>
    </div>
  </div>
</template>

<script>
import Lightgallery from "lightgallery/vue";
import lgThumbnail from "lightgallery/plugins/thumbnail";
import lgZoom from "lightgallery/plugins/zoom";
import HolidayCategorySaint from "@/components/holiday/HolidayCategorySaint.vue";
import HolidayCategorySaints from "@/components/holiday/HolidayCategorySaints.vue";
import HolidayCategoryGreatHoliday from "@/components/holiday/HolidayCategoryGreatHoliday.vue";
import { useTheme } from "vuetify";
import { imgUrl } from "@/utils/common";
import { isGreatHoliday } from "@/utils/holidays";
import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import ChipHolidayCategory from "@/components/holiday/ChipHolidayCategory.vue";
import ChipDay from "@/components/day/ChipDay.vue";

let lightGallery = null;
export default {
  components: {
    ListItemYear,
    Lightgallery,
    HolidayCategorySaint,
    HolidayCategorySaints,
    ListItemManuscript,
    HolidayCategoryGreatHoliday,
    ChipHolidayCategory,
    ChipDay
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  data: () => ({
    plugins: [lgThumbnail, lgZoom]
    // galleryContainer: this.$refs.galleryContainer
  }),
  computed: {
    isGreatHoliday() {
      return isGreatHoliday(this.holiday.holiday_category?.title);
    },
    CurrentHolidayCategory() {
      if (this.isGreatHoliday) {
        return HolidayCategoryGreatHoliday;
      } else if (this.holiday.saints?.length > 1) {
        return HolidayCategorySaints;
      } else {
        return HolidayCategorySaint;
      }
    }
  },
  setup() {
    const theme = useTheme();

    return {
      theme
    };
  },
  mounted() {
    if (this.isGreatHoliday) {
      this.theme.global.name.value = "myCustomLightTheme";
    }
  },
  methods: {
    imgUrl,
    onInit: (detail) => {
      lightGallery = detail.instance;
      // detail.instance.openGallery(0);
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

.gallery-item {
  margin: 5px
}
</style>


