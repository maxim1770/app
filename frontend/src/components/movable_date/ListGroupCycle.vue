<template>
  <v-list-group :value="cycle.num">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        class="ma-1 text-center"
      >
        <MainSmallTitle
          :title="cycle.title"
          textColor="red-darken-4"
        />
        <p
          class="text-blue-lighten-2 text-center ma-1"
          :style="{ 'font-size': !lgAndUp ? 'smaller' : 'medium' }"
        >
          {{ cycle?.desc }}
        </p>
      </v-list-item>
    </template>
    <slot></slot>
  </v-list-group>
</template>


<script>

import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import { useDisplay } from "vuetify";

export default {
  components: { MainSmallTitle },
  props: {
    cycle: {
      type: Object,
      required: true
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};
</script>