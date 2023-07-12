<template>
  <div>
    <lightgalleryWithDesc :imgs_data="allIcons" />
    <h4 class="text-h4 font-weight-bold ma-2">
      <SaintFullTitle :saint="saint" />
    </h4>
    <v-divider></v-divider>
    <div
      v-if="saint.holidays?.length"
      class="mt-2"
    >
      <h3>Дни памяти:</h3>
      <v-list lines="one">
        <v-list-item
          v-for="holiday in saint.holidays"
          :key="holiday.id"
          :to="{ name: 'holiday', params: { holidaySlug: holiday.slug } }"
          rounded="xl"
        >
          <v-chip>
            <HolidayFullTitle :holiday="holiday" />
          </v-chip>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
    </div>
    <div
      v-if="saint.books?.length"
      class="mt-2"
    >
      <h3>Труд:</h3>
      <v-list lines="one">
        <v-list-item
          v-for="book in saint.books"
          :key="book.id"
          :to="{ name: 'book', params: { bookId: book.id } }"
          rounded="xl"
        >
          <div>
            <BookFullTitleFactory :book="book" />
          </div>
        </v-list-item>
      </v-list>
    </div>
    <v-divider></v-divider>
  </div>
</template>

<script>

import lightgalleryBase from "@/components/lightgallery/lightgalleryBase.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";
import SaintFullTitle from "@/components/saint/SaintFullTitle.vue";
import lightgalleryWithDesc from "@/components/lightgallery/lightgalleryWithDesc.vue";


export default {
  components: {
    lightgalleryWithDesc,
    BookFullTitleFactory,
    lightgalleryBase,
    SaintFullTitle, HolidayFullTitle
  },
  props: {
    saint: {
      type: Object,
      required: true
    }
  },
  computed: {
    allIcons() {
      const allIcons_ = new Set();
      this.saint.holidays?.forEach((holiday) => {
        holiday.icons?.forEach((icon) => {
          allIcons_.add(icon);
        });
      });
      return allIcons_;
    }
  }
};
</script>

