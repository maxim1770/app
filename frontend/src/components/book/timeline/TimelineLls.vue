<template>
  <v-timeline
    :side="lgAndDown ? 'end' : undefined"
    align="start"
  >
    <v-timeline-item
      v-for="manuscript in llsManuscripts"
      :key="manuscript.id"
      dot-color="red-lighten-1"
      icon="mdi-bookshelf"
      size="small"
      fill-dot
    >
      <v-chip
        v-if="manuscript.code"
        :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
        :style="{ 'font-size': smAndDown ? 'smaller' : 'larger' }"
        color="blue"
        class="d-flex justify-center"
      >
        {{ manuscript.title }}
      </v-chip>
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import { useDisplay } from "vuetify";

export default {
  components: { ManuscriptFullTitle },
  props: {
    llsManuscripts: {
      type: Object,
      required: true
    }
  },
  setup() {
    const { smAndDown, lgAndDown } = useDisplay();
    return { smAndDown, lgAndDown };
  }
};

</script>



