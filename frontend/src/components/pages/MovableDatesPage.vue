<template>
  <div>
    <h5 class="text-h5 text-red-accent-4 font-weight-bold">
      Указатель Евангельских и Апостольских чтений на каждый день года
    </h5>
    <Cycle1And2 :cycle="movableDates[0]" />
    <Cycle1And2 :cycle="movableDates[1]" />
    <Cycle3 :cycle="movableDates[2]" />
  </div>
</template>

<script>

import Cycle1And2 from "@/components/movable_date/Cycle1And2.vue";
import Cycle3 from "@/components/movable_date/Cycle3.vue";

export default {

  components: { Cycle1And2, Cycle3 },

  props: {
    movableDates: {
      type: Object,
      required: true
    }
  }
};
</script>

