<template>
  <v-list-item>
    <template v-slot:prepend>
      <v-icon
        icon="mdi-candelabra-fire"
        :color="choiceHolidayColor(holiday)"
      />
    </template>
    <BadgeHolidayCategory :holiday_category="holiday.holiday_category" />
  </v-list-item>
</template>

<script>


import BadgeHolidayCategory from "@/components/holiday/holiday_category_title/BadgeHolidayCategory.vue";
import { choiceHolidayColor } from "@/utils/holidays";

export default {
  components: { BadgeHolidayCategory },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  methods: { choiceHolidayColor }
};

</script>



