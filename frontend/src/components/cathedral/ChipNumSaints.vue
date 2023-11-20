<template>
  <v-chip
    v-if="cathedral?.num_saints"
    color="red-lighten-1"
  >
    <BadgeNum
      :num="cathedral.num_saints"
      color="red-lighten-1"
      class="mr-1"
    />
    Святых Отцов
  </v-chip>
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";

export default {
  components: { BadgeNum },
  props: {
    cathedral: {
      type: Object,
      required: true
    }
  }
};

</script>



