<template>
  <v-timeline
    side="end"
    align="start"
  >
    <v-timeline-item
      v-for="material in materials"
      :key="material.link"
      @click="toUrl(material.link)"
      :icon="timelineItemIcon"
      :dot-color="material.highlight ? 'blue-darken-1' : 'blue-lighten-1'"
      :size="material.highlight ? 'default' : 'small'"
      fill-dot
    >
      <p
        :style="{ 'font-size': smAndDown ? 'medium' : 'larger' }"
        :class="{'font-weight-bold text-blue-darken-2': material.highlight}"
      >
        {{ material.title }}
      </p>
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import { useDisplay } from "vuetify";
import { toUrl } from "@/utils/common";

export default {
  props: {
    materials: {
      type: Array,
      required: true
    },
    timelineItemIcon: {
      type: String,
      required: true
    }
  },
  setup() {
    const smAndDown = useDisplay();
    return smAndDown;
  },
  methods: { toUrl }
};

</script>

