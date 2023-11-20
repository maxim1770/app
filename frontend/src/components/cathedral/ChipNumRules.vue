<template>
  <v-chip
    color="orange-lighten-1"
  >
    <BadgeNum
      :num="cathedral.num_rules"
      color="amber-lighten-2"
      class="mr-1"
    />
    Правил
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



