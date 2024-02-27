<template>
  <ExpansionPanelSearch @getItems="$emit('getItems')">
    <v-row>
      <v-col>
        <v-autocomplete
          @update:modelValue="$emit('update:year', $event)"
          :model-value="year"
          :items="[2031, 2032, 2033, 2034, 2035, 2036, 2037, 2038]"
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

