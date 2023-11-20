<template>
  <v-list>
    <v-list-item
      v-if="topTipikonHoliday?.slug"
      :to="{ name: 'holiday', params: { holidaySlug: topTipikonHoliday.slug } }"
      :color="choiceHolidayColor(topTipikonHoliday)"
    >
      <template v-slot:prepend>
        <v-icon
          v-if="topTipikonHoliday.tipikon"
          :icon="computeCustomIcon(topTipikonHoliday.tipikon?.title_en)"
        />
        <BadgeHolidayCategory
          v-else
          :holiday_category="topTipikonHoliday?.holiday_category"
        />
      </template>
      <BadgeHolidayCategory
        :holiday_category="topTipikonHoliday.holiday_category"
        class="ma-1"
      />
      <span
        :class="choiceHolidayTextColor(topTipikonHoliday)"
        class="ma-1"
      >
        {{ topTipikonHoliday?.title }}
      </span>
      <ChipYear
        :year="topTipikonHoliday?.year"
        class="ma-1"
      />
    </v-list-item>
  </v-list>
</template>

<script>

import { choiceHolidayColor, choiceHolidayTextColor, prepareDateAllSortedHolidays } from "@/utils/holidays";
import ChipYear from "@/components/year/ChipYear.vue";
import BadgeHolidayCategory from "@/components/holiday/holiday_category_title/BadgeHolidayCategory.vue";
import { computeCustomIcon } from "@/utils/common";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle, BadgeHolidayCategory, ChipYear },
  props: {
    mainData: {
      type: Object,
      required: true
    }
  },
  computed: {
    topTipikonHoliday() {
      return this.__allHolidays?.[0];
    },
    __allHolidays() {
      return prepareDateAllSortedHolidays(this.mainData?.date);
    }
  },
  methods: { choiceHolidayTextColor, choiceHolidayColor, computeCustomIcon }
};

</script>


