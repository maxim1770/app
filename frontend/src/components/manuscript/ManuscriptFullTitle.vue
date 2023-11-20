<template>
  <span class="ma-1">{{ manuscript?.title }}</span>
  <ChipYear :year="manuscript?.year" class="ma-1" />
  <ChipHandwritingTitle :manuscript="manuscript" class="ma-1" />
  <ChipNumBookmarks :manuscript="manuscript" class="ma-1" />
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";
import ChipHandwritingTitle from "@/components/manuscript/handwriting/ChipHandwritingTitle.vue";
import ChipNumBookmarks from "@/components/bookmark/num_bookmarks/ChipNumBookmarks.vue";

export default {
  components: { ChipYear, ChipHandwritingTitle, ChipNumBookmarks },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



