<template>
  <component
    :is="chapterFactory"
    v-if="holidays?.length"
    headTitle="Праздники"
  >
    <v-card>
      <v-card-item>
        <v-list>
          <v-list-item
            v-for="holiday in holidays"
            :key="holiday.id"
            :to="{ name: 'holiday', params: { holidaySlug: holiday.slug } }"
          >
            <template v-slot:prepend>
              <v-icon
                icon="mdi-candelabra-fire"
                :color="choiceHolidayColor(holiday)"
              />
            </template>
            <HolidayFullTitle :holiday="holiday" />
          </v-list-item>
        </v-list>
      </v-card-item>
    </v-card>
  </component>
</template>


<script>


import HolidayFullTitle from "@/components/holiday/HolidayFullTitle.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import { choiceHolidayColor } from "@/utils/holidays";

export default {
  components: { ChapterWithHead, HolidayFullTitle },
  props: {
    holidays: {
      type: Array,
      required: true
    },
    hasHeadTitle: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  computed: {
    chapterFactory() {
      return this.hasHeadTitle ? ChapterWithHead : "span";
    }
  },
  methods: {
    choiceHolidayColor
  }
};

</script>


