<template>
  <v-chip
    v-if="manuscript.num_bookmarks"
    :color="ChipNumBookmarksColor"
    prepend-icon="mdi-book-outline"
  >
    {{ manuscript.num_bookmarks_title }}
  </v-chip>
</template>

<script>


import UnfoldBtns from "@/components/common/UnfoldBtns.vue";

export default {
  components: { UnfoldBtns },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  computed: {
    ChipNumBookmarksColor() {
      switch (this.manuscript.num_bookmarks) {
        case 4:
          return "green-accent-4";
        case 3:
          return "green-accent-4";
        case 2:
          return "green-accent-2";
        case 1:
          return "green-accent-1";
      }
    }
  }
};

</script>



