<template>
  <strong
    :class="isVselenskijSobor(Cathedral) ? 'text-red-darken-4' : null"
    class="ma-1"
  >
    {{ Cathedral.title }}
  </strong>
  <ChipYear
    v-if="has_show_year"
    :year="Cathedral.year"
    class="ma-1"
  />
  <ChipNumSaints
    :cathedral="Cathedral"
    class="ma-1"
  />
  <ChipNumRules
    :cathedral="Cathedral"
    class="ma-1"
  />
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";
import ChipYear from "@/components/year/ChipYear.vue";
import ChipNumSaints from "@/components/cathedral/ChipNumSaints.vue";
import ChipNumRules from "@/components/cathedral/ChipNumRules.vue";
import { isVselenskijSobor } from "@/utils/common";

export default {
  components: { ChipNumRules, ChipNumSaints, ChipYear, BadgeNum },
  props: {
    cathedral: {
      type: Object,
      required: false,
      default: null
    },
    book: {
      type: Object,
      required: false,
      default: null
    },
    has_show_year: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  computed: {
    Cathedral() {
      return this.cathedral || this.book.cathedral_book.cathedral;
    }
  },
  methods: { isVselenskijSobor }
};

</script>



