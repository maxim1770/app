<template>
  <v-chip
    v-if="chapter_num"
    color="red-darken-1"
  >
    Глава
    <BadgeNum :num="chapter_num" color="red-lighten-2" class="ml-1" />
  </v-chip>
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";

export default {
  components: { BadgeNum },
  props: {
    chapter_num: {
      type: Number,
      required: true
    }
  }
};

</script>



