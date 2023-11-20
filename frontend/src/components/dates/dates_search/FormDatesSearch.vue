<template>
  <ExpansionPanelSearch @getItems="$emit('getItems')">
    <v-row>
      <v-col
        cols="6"
        offset="6"
        md="4"
        offset-md="8"
      >
        <v-autocomplete
          @update:modelValue="$emit('update:year', $event)"
          :model-value="year"
          :items="[2031, 2032, 2033]"
          label="Год"
        />
      </v-col>
    </v-row>
  </ExpansionPanelSearch>
</template>


<script>


import ExpansionPanelSearch from "@/components/search/ExpansionPanelSearch.vue";

export default {
  components: { ExpansionPanelSearch },
  props: {
    year: {
      type: Number,
      required: true
    }
  },
  emits: [
    "update:year",
    "getItems"
  ]
};

</script>

