<template>
  {{ manuscript?.title }}
  <ChipYear :year="manuscript?.year" class="ml-1" />
  <ChipHandwritingTitle v-if="manuscript?.handwriting_title" :manuscript="manuscript" class="ml-1" />
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";
import ChipHandwritingTitle from "@/components/manuscript/ChipHandwritingTitle.vue";

export default {
  components: { ChipYear, ChipHandwritingTitle },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



