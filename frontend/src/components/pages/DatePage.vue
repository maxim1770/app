<template>
  <div class="mt-2">
    <div class="d-flex justify-space-evenly align-center">
      <v-btn
        @click="$router.push({ name: 'date', params: { date: preDate } })"
        prepend-icon="mdi-arrow-left"
      >
        Вчера
      </v-btn>
      <v-card elevation="4">
        <v-card-item class="text-center">
          <v-card-title>
            <h3>{{ date.day?.title }}</h3>
          </v-card-title>
          <v-card-title>
            <h3>{{ date.movable_day?.full_title }}</h3>
          </v-card-title>
          <v-card-title>
            <h3>{{ date.movable_day?.week.sunday_title }}</h3>
          </v-card-title>
          <v-divider></v-divider>
          <v-card-subtitle>
            {{ date.movable_day?.week.title }}
          </v-card-subtitle>
        </v-card-item>
        <v-card-text class="text-center text-subtitle-1">
          <template v-if="date.post">{{ date.post.title }}</template>
          <template v-else>Поста нет</template>
        </v-card-text>
      </v-card>
      <v-btn
        @click="$router.push({ name: 'date', params: { date: nextDate } })"
        append-icon="mdi-arrow-right"
      >
        Завтра
      </v-btn>
    </div>
    <TableDateHolidaysToMe :date="date" />
    <v-divider></v-divider>
    <div class="mt-2">
      <v-divider></v-divider>
      <v-list>
        <v-list-item
          v-if="before_after_holiday"
          :to="{ name: 'holiday', params: { holidaySlug: before_after_holiday.holiday.slug } }"
          rounded="xl"
          class="mb-1 bg-red-accent-2"
        >
          <HolidayFullTitle :holiday="before_after_holiday.holiday" />
          <v-divider class="mt-1"></v-divider>
        </v-list-item>
        <v-list-item
          v-for="holiday in allHolidays"
          :key="holiday.id"
          :to="{ name: 'holiday', params: { holidaySlug: holiday.slug } }"
          rounded="xl"
          class="mb-1"
          :class="{
          'bg-red-accent-4': isGreatHoliday(holiday.holiday_category?.title)
        }"
        >
          <HolidayFullTitle :holiday="holiday" />
          <v-divider class="mt-1"></v-divider>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>
    </div>
    <div
      v-if="date.movable_day?.movable_dates?.length"
      class="mt-2"
    >
      <h3>Чтения Священного Писания:</h3>
      <v-container
        class="rounded-lg border text-center text-red-accent-3 mt-1"
      >
        <CurrentWeekFactory :week="date.movable_day.week" :currentMovableDayAbbr="date.movable_day.abbr" />
      </v-container>
    </div>
    <v-divider></v-divider>
    <div
      v-if="date.movable_day?.movable_date_books?.length"
      class="mt-2"
    >
      <h3>Чтения по времени:</h3>
      <div
        v-for="movable_date_book in date.movable_day?.movable_date_books"
        :key="movable_date_book.id"
      >
        <v-list-item
          prepend-icon="mdi-book-heart-outline"
        >
          <v-chip variant="tonal" color="blue">
            {{ movable_date_book?.book.type }}
          </v-chip>
        </v-list-item>
        <v-list lines="one">
          <ListItemManuscript :manuscript="movable_date_book.book.bookmarks?.[0].manuscript" />
        </v-list>
        <!--        <lightgalleryBase :imgs="movable_date_book.book.bookmarks?.[0].imgs_paths" />-->
        <v-divider></v-divider>
      </div>
    </div>
    <v-divider></v-divider>
  </div>
</template>

<script>

import { nextDate, preDate } from "@/utils/date";
import ChipYear from "@/components/year/ChipYear.vue";
import { isGreatHoliday } from "@/utils/holidays";
import ChipHolidayCategory from "@/components/holiday/ChipHolidayCategory.vue";
import TableDateHolidaysToMe from "@/components/date/TableDateHolidaysToMe.vue";
import lightgalleryBase from "@/components/lightgallery/lightgalleryBase.vue";
import CurrentWeekFactory from "@/components/movable_date/week/CurrentWeekFactory.vue";
import strastnajaSedmitsa from "@/components/movable_date/week/strastnajaSedmitsa.vue";
import ListItemManuscript from "@/components/manuscript/ListItemManuscript.vue";
import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";


export default {
  components: {
    HolidayFullTitle,
    ListItemManuscript,
    strastnajaSedmitsa,
    ChipYear,
    ChipHolidayCategory,
    TableDateHolidaysToMe,
    lightgalleryBase,
    CurrentWeekFactory
  },
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  computed: {
    allHolidays() {
      let allHolidays_ = [];
      if (this.date.day?.holidays) {
        allHolidays_ = allHolidays_.concat(this.date.day.holidays);
      }
      if (this.date.movable_day?.holidays) {
        allHolidays_ = allHolidays_.concat(this.date.movable_day.holidays);
      }
      return allHolidays_;
    },
    currentStrDate() {
      return this.$route.params.date;
    },
    preDate() {
      return preDate(this.currentStrDate);
    },
    nextDate() {
      return nextDate(this.currentStrDate);
    },
    before_after_holiday() {
      let before_after_holiday = null;
      if (this.date.day?.before_after_holidays?.[0]?.before_after_holiday) {
        before_after_holiday = this.date.day?.before_after_holidays[0].before_after_holiday;
      } else if (this.date.movable_day?.before_after_holidays?.[0]?.before_after_holiday) {
        before_after_holiday = this.date.movable_day?.before_after_holidays[0].before_after_holiday;
      }
      return before_after_holiday;
    }
  },
  methods: {
    isGreatHoliday
  }
};
</script>
