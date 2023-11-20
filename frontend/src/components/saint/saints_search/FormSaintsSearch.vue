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
          @update:modelValue="$emit('update:face_sanctity__title', $event)"
          :model-value="face_sanctity__title"
          :items="saintsSearchData.face_sanctity_titles"
          label="Сан"
        ></v-autocomplete>
      </v-col>
      <v-col
        cols="12"
        md="6"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:dignity__title', $event)"
          :model-value="dignity__title"
          :items="saintsSearchData.dignity_titles"
          label="Лик Святости"
        ></v-autocomplete>
      </v-col>
    </v-row>
    <!--        <v-col-->
    <!--          cols="12"-->
    <!--          md="3"-->
    <!--        >-->
    <!--          <v-autocomplete-->
    <!--            v-model="selected_order_by"-->
    <!--            label="Сортировать"-->
    <!--            :items=Object.keys(ORDER_BY_TITLES)-->
    <!--            multiple-->
    <!--            clearable-->
    <!--            chips-->
    <!--            variant="solo"-->
    <!--          ></v-autocomplete>-->
    <!--        </v-col>-->
  </ExpansionPanelSearch>
</template>


<script>


import TextFieldSearch from "@/components/search/TextFieldSearch.vue";
import ExpansionPanelSearch from "@/components/search/ExpansionPanelSearch.vue";

export default {
  components: { ExpansionPanelSearch, TextFieldSearch },
  props: {
    saintsSearchData: {
      type: Object,
      required: true
    },
    face_sanctity__title: {
      type: String,
      required: true
    },
    dignity__title: {
      type: String,
      required: true
    },
    search: {
      type: String,
      required: true
    }
  },
  emits: [
    "update:face_sanctity__title",
    "update:dignity__title",
    "update:search",
    "getItems"
  ]
};

</script>





