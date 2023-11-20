<template>
  <v-chip
    color="blue-grey-lighten-3"
  >
    л.
    <BadgeNum
      :num="first_page.num"
      color="blue-grey-lighten-2"
      class="ml-1"
    />
  </v-chip>
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";

export default {
  components: { BadgeNum },
  props: {
    first_page: {
      type: Object,
      required: true
    }
  }
};

</script>



