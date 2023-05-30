<template>
  <div class="d-block d-lg-flex flex-wrap justify-center">
    <v-card
      v-for="holiday in holidays"
      :key="holiday.id"
      class="mb-2 pa-2"
      :class="{ 'w-25 ma-5': xlAndUp }"
    >
      <ImgWithPlaceholder :src="imgUrl(holiday.icons?.[0]?.path)" />
      <v-card-text>
        <p class="text-h6 text-center mb-2">{{ holiday.title }}</p>
        <div class="d-table">
          <v-chip variant="tonal" class="mx-2 my-1" color="green">
            {{ holiday.holiday_category?.title }}
          </v-chip>
          <v-chip variant="tonal" class="mx-2 my-1" color="cyan">
            {{ holiday.year?.title }}
          </v-chip>
          <v-chip
            @click="$router.push({
                name: 'date',
                params: { date: holiday.day?.month_day },
              })"
            variant="tonal"
            class="mx-2 my-1"
            color="teal"
          >
            {{ holiday.day?.title }}
          </v-chip>
        </div>
        <v-list lines="one">
          <v-list-item
            v-for="saint in holiday.saints"
            :key="saint.id"
            :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
          >
            {{ saint.slug }}
          </v-list-item>
        </v-list>
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn
          @click="
            $router.push({
              name: 'holiday',
              params: { holidaySlug: holiday.slug },
            })
          "
          color="secondary"
          rounded="lg"
        >
          Перейти
        </v-btn>
      </v-card-actions>
    </v-card>
  </div>
</template>

<script>
import { useDisplay } from "vuetify";
import ImgWithPlaceholder from "@/components/common/ImgWithPlaceholder.vue";
import { imgUrl } from "@/utils/common";

export default {
  components: { ImgWithPlaceholder },
  props: {
    holidays: {
      type: Object,
      required: true
    }
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  methods: { imgUrl }
};
</script>
