<template>
  <v-list-group :value="cycle.num">
    <template v-slot:activator="{ props }">
      <v-list-item
        v-bind="props"
        class="ma-1 text-center"
      >
        <MainSmallTitle
          :title="cycle.title"
          textColor="red-darken-2"
        />
        <p class="text-center font-weight-bold ma-1 ">
          {{ cycle?.desc }}
        </p>
      </v-list-item>
    </template>
    <slot></slot>
  </v-list-group>
</template>


<script>

import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle },
  props: {
    cycle: {
      type: Object,
      required: true
    }
  }
};
</script>