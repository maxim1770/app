<template>
  <ExpansionPanelSearch @getItems="$emit('getItems')">
    <v-row>
      <v-col>
        <TextFieldSearch
          :search="search"
          @update:search="$emit('update:search', $event)"
        />
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:tipikon__title', $event)"
          :model-value="tipikon__title"
          :items="tipikonTitlesWithIcons"
          item-props
          label="Типикон"
        ></v-autocomplete>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:holiday_category__title', $event)"
          :model-value="holiday_category__title"
          :items="holidaysSearchData.holiday_category_titles"
          label="Категория"
        ></v-autocomplete>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <DaySearch
          :day__month="day__month"
          :day__day="day__day"
        />
      </v-col>
    </v-row>
  </ExpansionPanelSearch>
</template>


<script>


import TextFieldSearch from "@/components/search/TextFieldSearch.vue";
import ExpansionPanelSearch from "@/components/search/ExpansionPanelSearch.vue";
import DaySearch from "@/components/holiday/holidays_search/DaySearch.vue";
import { computeCustomIcon } from "@/utils/common";

export default {
  components: { DaySearch, ExpansionPanelSearch, TextFieldSearch },
  props: {
    holidaysSearchData: {
      type: Object,
      required: true
    },
    search: {
      type: String,
      required: true
    },
    tipikon__title: {
      type: String,
      required: true
    },
    holiday_category__title: {
      type: String,
      required: true
    },
    day__month: {
      type: Number,
      required: true
    },
    day__day: {
      type: Number,
      required: true
    }
  },
  emits: [
    "update:search",
    "update:tipikon__title",
    "update:holiday_category__title",
    "getItems"
  ],
  computed: {
    tipikonTitlesWithIcons() {
      let tipikonTitlesWithIcons = [];
      for (let tipikon of this.holidaysSearchData.tipikons) {
        tipikonTitlesWithIcons.push({
          prependIcon: computeCustomIcon(tipikon.title_en),
          title: tipikon.title
        });
      }
      return tipikonTitlesWithIcons;
    }
  }
};

</script>

