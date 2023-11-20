<template>
  <v-list-item
    prepend-icon="mdi-pencil-outline"
  >
    Почерк
    <RatingHandwriting :handwriting_to_rating="manuscript?.handwriting_to_rating" class="ma-1" />
    <ChipHandwritingTitle :manuscript="manuscript" class="ma-1" />
  </v-list-item>
</template>

<script>


import BadgeFaceSanctity from "@/components/saint/face_sanctity/BadgeFaceSanctity.vue";
import RatingHandwriting from "@/components/manuscript/handwriting/RatingHandwriting.vue";
import ChipHandwritingTitle from "@/components/manuscript/handwriting/ChipHandwritingTitle.vue";

export default {
  components: { ChipHandwritingTitle, RatingHandwriting, BadgeFaceSanctity },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>






