<template>
  <v-expansion-panels
    :model-value="panel"
  >
    <v-expansion-panel>
      <v-expansion-panel-title
        expand-icon="mdi-filter-plus"
        collapse-icon="mdi-filter-minus"
      >
        <v-icon icon="mdi-magnify"></v-icon>
        <p class="ml-3 text-body-1">Поиск</p>
      </v-expansion-panel-title>
      <v-expansion-panel-text>
        <v-form>
          <v-container>
            <slot></slot>
            <RowSubmitAndClearBtns @getItems="$emit('getItems')" />
          </v-container>
        </v-form>
      </v-expansion-panel-text>
    </v-expansion-panel>
  </v-expansion-panels>
</template>


<script>


import RowSubmitAndClearBtns from "@/components/search/RowSubmitAndClearBtns.vue";
import { numObjectKeys } from "@/utils/common";

export default {
  components: { RowSubmitAndClearBtns },
  emits: ["getItems"],
  data() {
    return {
      panel: []
    };
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
      if (numObjectKeys(newVal)) {
        this.panel.push(0);
      }
    }
  }
};

</script>

