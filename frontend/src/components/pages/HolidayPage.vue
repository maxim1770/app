<template>
  <div>
    <lightgalleryWithDesc :imgs_data="holiday.holiday?.icons" />
    <h4 class="text-h4 font-weight-bold ma-2">
      {{ holiday.holiday?.title }}
      <ChipHolidayCategory
        :holiday_category="holiday.holiday?.holiday_category"
        class="ml-1"
        :class="{
      'text-red-darken-3': isGreatHoliday,
      'text-green': !isGreatHoliday
      }"
      />
    </h4>
    <v-divider></v-divider>
    <div
      class="my-2"
    >
      <v-sheet class="bg-blue-lighten-2 pa-12" rounded>
        <v-card class="mx-auto px-6 py-8" max-width="500">
          <div>
            <v-select
              v-model="tipikon_title"
              :items="holiday.tipikon_titles"
              class="mb-2"
              clearable
              label="Выберите Типикон Праздника"
              variant="underlined"
            ></v-select>
            <br>
            <v-btn
              @click="putHoliday"
              block
              color="success"
              size="large"
              type="submit"
              variant="elevated"
            >
              Обновить
            </v-btn>
            <ListItemTipikon v-if="holiday.holiday?.tipikon" :tipikon="holiday.holiday.tipikon" />
          </div>
        </v-card>
      </v-sheet>
    </div>
    <v-divider></v-divider>
    <HolidayFactory :holiday="holiday.holiday" />
    <div
      v-if="holiday.holiday?.holiday_books.length"
      class="mt-2"
    >
      <h3>Жития, Прологи:</h3>
      <div
        v-for="holiday_book in holiday.holiday.holiday_books"
        :key="holiday_book.id"
      >
        <v-list lines="one">
          <v-list-item
            v-if="holiday_book?.book.title === 'Пролог'"
            prepend-icon="mdi-book-heart-outline"
          >
            <v-chip variant="tonal" color="blue">
              Пролог
            </v-chip>
          </v-list-item>
          <v-list-item
            v-if="holiday_book?.book_util === 'Упоминание'"
            prepend-icon="mdi-alert-outline"
          >
            <v-chip variant="tonal" color="red">
              Только упоминание
            </v-chip>
          </v-list-item>
          <ListItemManuscript :manuscript="holiday_book.book.bookmarks?.[0].manuscript" />
        </v-list>
        {{ holiday_book.book.bookmarks?.[0].imgs_paths }}
        <!--        <lightgalleryBase :imgs="holiday_book.book.bookmarks?.[0].imgs_paths" />-->
        <v-divider></v-divider>
      </div>
    </div>
    <div
      v-if="holiday.holiday?.molitva_books_ !== null"
      class="mt-2"
    >
      <h3>Тропари, кондаки:</h3>
      <div
        v-for="(molitva_books, manuscript_code, index) in holiday.holiday?.molitva_books_"
        :key="index"
      >
        <v-list lines="one">
          <v-list-item
            v-for="molitva_book in molitva_books"
            :key="molitva_book.id"
            prepend-icon="mdi-book-open-variant"
          >
            <v-chip class="ml-1">
              {{ molitva_book.title }}
            </v-chip>
          </v-list-item>
          <v-divider inset></v-divider>
          <ListItemManuscript :manuscript="molitva_books?.[0].book.bookmarks?.[0].manuscript" />
        </v-list>
        <!--        {{ commonManuscriptImgsPaths(molitva_books) }}-->
        <lightgalleryBase :imgs="commonManuscriptImgsPaths(molitva_books)" />
        <v-divider></v-divider>
      </div>
    </div>
  </div>
</template>

<script>

import { useTheme } from "vuetify";
import { isGreatHoliday } from "@/utils/holidays";
import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import ChipHolidayCategory from "@/components/holiday/ChipHolidayCategory.vue";
import ChipDay from "@/components/day/ChipDay.vue";
import lightgalleryBase from "@/components/lightgallery/lightgalleryBase.vue";
import lightgalleryWithDesc from "@/components/lightgallery/lightgalleryWithDesc.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";
import HolidayFactory from "@/components/holiday/holiday/HolidayFactory.vue";
import { api } from "@/services/api";
import ListItemTipikon from "@/components/tipikon/ListItemTipikon.vue";

export default {
  components: {
    ListItemTipikon,
    HolidayFactory,
    HolidayFullTitle,
    BookFullTitleFactory,
    lightgalleryBase,
    lightgalleryWithDesc,
    ListItemYear,
    ListItemManuscript,
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
    tipikon_title: null
  }),
  computed: {
    isGreatHoliday() {
      return isGreatHoliday(this.holiday.holiday?.holiday_category.title);
    }
  },
  setup() {
    const theme = useTheme();
    return { theme };
  },
  mounted() {
    if (this.isGreatHoliday) {
      this.theme.global.name.value = "myCustomLightTheme";
    }
  },
  methods: {
    commonManuscriptImgsPaths(molitva_books) {
      const commonManuscriptImgsPaths_ = new Set();
      molitva_books?.forEach((molitva_book) => {
        molitva_book.book.bookmarks?.[0].imgs_paths.forEach(img_path => {
          commonManuscriptImgsPaths_.add(img_path);
        });
      });
      return commonManuscriptImgsPaths_;
    },
    putHoliday() {
      api
        .putHoliday({ "holidaySlug": this.$route.params.holidaySlug, "tipikon_title": this.tipikon_title })
        .then((response) => (this.holiday.holiday = response.data));
    }
  }
};
</script>



