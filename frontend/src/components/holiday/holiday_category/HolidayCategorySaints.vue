<template>
  <ChapterWithHead headTitle="Святые">
    <ListSaints :saints="holiday.saints" :holiday="holiday" />
  </ChapterWithHead>
</template>

<script>

import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ListSaints from "@/components/saint/ListSaints.vue";

export default {
  components: { ListSaints, ChapterWithHead },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>

