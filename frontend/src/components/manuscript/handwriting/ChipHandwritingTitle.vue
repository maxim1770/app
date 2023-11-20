<template>
  <v-chip
    v-if="manuscript.handwriting_title"
    :color="ChipHandwritingTitleColor"
    prepend-icon="mdi-pencil-outline"
  >
    {{ manuscript.handwriting_title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    ChipHandwritingTitleColor() {
      switch (this.manuscript.handwriting) {
        case 12:
        case 11:
          return "red-accent-4";
        case 10:
        case 9:
          return "red-accent-3";
        case 8:
        case 7:
          return "red-accent-2";
        default:
          return "red-accent-1";
      }
    }
  }
};

</script>



