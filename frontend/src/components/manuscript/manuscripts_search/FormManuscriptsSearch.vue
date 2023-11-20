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
          @update:modelValue="$emit('update:fund__library', $event)"
          :model-value="fund__library"
          :items="manuscriptsSearchData.library_titles"
          label="Библиотека"
        ></v-autocomplete>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:fund__title', $event)"
          :model-value="fund__title"
          :items="manuscriptsSearchData.fund_titles"
          label="Фонд"
        ></v-autocomplete>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <YearsRangeSearch
          :y__year__gte="y__year__gte"
          :y__year__lt="y__year__lt"
          @update:y__year__gte="$emit('update:y__year__gte', $event)"
          @update:y__year__lt="$emit('update:y__year__lt', $event)"
        />
      </v-col>
    </v-row>
  </ExpansionPanelSearch>
</template>


<script>


import TextFieldSearch from "@/components/search/TextFieldSearch.vue";
import ExpansionPanelSearch from "@/components/search/ExpansionPanelSearch.vue";
import YearsRangeSearch from "@/components/manuscript/manuscripts_search/YearsRangeSearch.vue";

export default {
  components: { YearsRangeSearch, ExpansionPanelSearch, TextFieldSearch },
  props: {
    manuscriptsSearchData: {
      type: Object,
      required: true
    },
    fund__title: {
      type: String,
      required: true
    },
    fund__library: {
      type: String,
      required: true
    },
    search: {
      type: String,
      required: true
    },
    y__year__gte: {
      type: Number,
      required: true
    },
    y__year__lt: {
      type: Number,
      required: true
    }

  },
  emits: [
    "update:search",
    "update:fund__title",
    "update:fund__library",
    "update:y__year__gte",
    "update:y__year__lt",
    "getItems"
  ]
};

</script>

