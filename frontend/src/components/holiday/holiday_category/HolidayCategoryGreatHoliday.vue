<template>
  <ChapterWithHead :headTitle="`Другие ${ holiday.holiday_category.title}`">
    <v-card>
      <v-card-item>
        <v-list>
          <v-list-item
            :to="{ name: 'saint', params: { saintSlug: holiday.saints[0].slug } }"
          >
            <template v-slot:prepend>
              <v-icon
                icon="mdi-candelabra-fire"
                :color="choiceHolidayColor(holiday)"
                size="large"
              />
            </template>
            <span
              :class="choiceHolidayTextColor(holiday)"
              class="ma-1"
            >
              {{ holiday.saints[0].name }}
            </span>
          </v-list-item>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import { choiceHolidayColor, choiceHolidayTextColor } from "@/utils/holidays";

export default {
  components: { ChapterWithHead },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  methods: { choiceHolidayTextColor, choiceHolidayColor }
};

</script>



