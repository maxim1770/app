<template>
  <v-card class="d-flex justify-center align-center my-3">
    <v-btn
      v-if="date?.date_slug"
      @click="$router.push({ name: 'date', params: { dateSlug: preDateSlug } })"
      prepend-icon="mdi-arrow-left"
      size="small"
      rounded="xl"
      elevation="4"
      class="text-none ml-2"
    >
      <span v-if="lgAndUp">Предыдущий день</span>
    </v-btn>
    <div>
      <v-card-item class="text-center">
        <v-card-title>
          <MainBigTitle :title="date.day?.title" textColor="red-accent-4" :hasDivider="false" />
          <v-chip
            v-if="date.movable_day?.week?.sunday_title"
            color="red-accent-4"
          >
            {{ date.movable_day.week.sunday_title }}
          </v-chip>
          <MainSmallTitle :title="date.movable_day?.full_title" />
        </v-card-title>
        <v-divider />
        <v-card-subtitle>
          {{ date.movable_day?.week.title }}
        </v-card-subtitle>
      </v-card-item>
      <v-card-text class="text-center text-subtitle-1">
        <v-badge color="blue">
          <template v-slot:badge>
            <template v-if="date.post">{{ date.post.title }}</template>
            <template v-else>Поста нет</template>
          </template>
        </v-badge>
      </v-card-text>
    </div>
    <v-btn
      v-if="date?.date_slug"
      @click="$router.push({ name: 'date', params: { dateSlug: nextDateSlug } })"
      append-icon="mdi-arrow-right"
      size="small"
      rounded="xl"
      elevation="4"
      class="text-none mr-2"
    >
      <span v-if="lgAndUp">Следующий день</span>
    </v-btn>
  </v-card>
</template>

<script>

import { useDisplay } from "vuetify";
import { nextDateSlug, preDateSlug } from "@/utils/date";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import MainBigTitle from "@/components/common/title/MainBigTitle.vue";

export default {
  components: { MainBigTitle, MainTitle, MainSmallTitle },
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
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>



