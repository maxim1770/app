<template>
  <ChapterWithHead
    v-if="saint"
    :headTitle="headTitle"
  >
    <CardSaint :saint="saint" :holiday="holiday"/>
  </ChapterWithHead>
</template>


<script>

import CardSaint from "@/components/saint/CardSaint.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";

export default {
  components: { ChapterWithHead, CardSaint },
  props: {
    saint: {
      type: Object,
      required: true
    },
    holiday: {
      type: Object,
      required: false,
      default: null
    },
    headTitle: {
      type: String,
      required: true
    }
  }
};

</script>