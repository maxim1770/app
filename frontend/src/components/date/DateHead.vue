<template>
  <v-card class="d-flex justify-center align-center my-3">
    <v-btn
      v-if="date?.date_slug"
      @click="$router.push({ name: 'date', params: { dateSlug: preDateSlug } })"
      size="small"
      rounded="xl"
      elevation="4"
      class="text-none ml-2"
    >
      <template
        v-if="lgAndUp"
        v-slot:prepend
      >
        <v-icon
          icon="mdi-arrow-left"
          size="large"
        />
      </template>
      <span
        v-if="lgAndUp"
      >
        Предыдущий день
      </span>
      <v-icon
        v-if="!lgAndUp"
        icon="mdi-arrow-left"
        size="large"
      />
    </v-btn>
    <v-card-item
      class="text-center my-2"
    >
      <MainBigTitle
        :title="date.day?.title"
        textColor="red-darken-4"
        :hasDivider="false"
        :hasMargin="false"
      >
        <v-tooltip
          activator="parent"
          location="top"
        >
          Новый день начинается с вечера
        </v-tooltip>
      </MainBigTitle>
      <v-card-subtitle
        :style="{ 'font-size': !lgAndUp ? 'smaller' : 'medium' }"
      >
        {{ date.year_title }}
      </v-card-subtitle>
      <v-chip
        v-if="isSunDate && date.movable_day?.week?.sunday_title"
        color="red-accent-4"
        class="ma-1"
        :style="{ 'font-size': !lgAndUp ? 'small' : 'medium' }"
      >
        {{ date.movable_day.week.sunday_title }}
      </v-chip>
      <v-chip
        v-if="!isSunDate && date.movable_day?.title"
        color="red-accent-4"
        class="ma-1"
        :style="{ 'font-size': !lgAndUp ? 'small' : 'medium' }"
      >
        {{ date.movable_day?.title }}
      </v-chip>
      <component
        v-if="date.movable_day?.title !== date.movable_day?.full_title"
        :is="TitleSizeFactory"
        :title="date.movable_day?.full_title"
        :text-color="isSunDate ? 'red-accent-4' : 'blue-lighten-2'"
        :hasMargin="false"
      />
      <v-divider class="ma-1" />
      <v-card-subtitle
        v-if="!isSunDate"
        :style="{ 'font-size': !lgAndUp ? 'smaller' : 'larger' }"
      >
        {{ date.movable_day?.week.title }}
      </v-card-subtitle>
      <div>
        <ChipSolidWeek :is_solid_week="date.is_solid_week" />
      </div>
      <BadgePost
        :post="date.post"
        :date="date"
        class="mt-1"
      />
    </v-card-item>
    <v-btn
      v-if="date?.date_slug"
      @click="$router.push({ name: 'date', params: { dateSlug: nextDateSlug } })"
      size="small"
      rounded="xl"
      elevation="4"
      class="text-none mr-2"
    >
      <template
        v-if="lgAndUp"
        v-slot:append
      >
        <v-icon
          icon="mdi-arrow-right"
          size="large"
        />
      </template>
      <span
        v-if="lgAndUp"
      >
        Следующий день
      </span>
      <v-icon
        v-if="!lgAndUp"
        icon="mdi-arrow-right"
        size="large"
      />
    </v-btn>
  </v-card>
</template>

<script>

import { useDisplay } from "vuetify";
import { isSunDate, nextDateSlug, preDateSlug } from "@/utils/date";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import MainBigTitle from "@/components/common/title/MainBigTitle.vue";
import BadgePost from "@/components/post/BadgePost.vue";
import ChipSolidWeek from "@/components/date/ChipSolidWeek.vue";

export default {
  components: { ChipSolidWeek, BadgePost, MainBigTitle, MainTitle, MainSmallTitle },
  props: {
    date: {
      type: Object,
      required: true
    }
  },
  computed: {
    preDateSlug() {
      return preDateSlug(this.date?.date_slug);
    },
    nextDateSlug() {
      return nextDateSlug(this.date?.date_slug);
    },
    isSunDate() {
      return isSunDate(this.date);
    },
    TitleSizeFactory() {
      return this.isSunDate ? MainTitle : MainSmallTitle;
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>
