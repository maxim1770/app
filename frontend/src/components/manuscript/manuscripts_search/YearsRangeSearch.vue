<template>
  <v-range-slider
    @update:modelValue="updateYearsRange"
    :model-value="yearsRange"
    :ticks="smAndDown ? LESS_CENTURIES : CENTURIES"
    :min="MIN_YEAR"
    :max="MAX_YEAR"
    :step="5"
    color="blue"
    show-ticks="always"
    thumb-label="always"
    tick-size="5"
    hide-details
  >
  </v-range-slider>
</template>


<script>


import { YEAR_CHRISTMAS } from "@/utils/date";
import { useDisplay } from "vuetify";

export default {
  props: {
    y__year__gte: {
      type: Number,
      required: true
    },
    y__year__lt: {
      type: Number,
      required: true
    }

  },
  emits: [
    "update:y__year__gte",
    "update:y__year__lt"
  ],
  computed: {
    yearsRange() {
      return [
        typeof this.y__year__gte !== "undefined" ? this.y__year__gte - YEAR_CHRISTMAS : this.MIN_YEAR,
        typeof this.y__year__lt !== "undefined" ? this.y__year__lt - YEAR_CHRISTMAS : this.MAX_YEAR
      ];
    },
    YEAR_CHRISTMAS() {
      return YEAR_CHRISTMAS;
    }
  },
  created() {
    this.MIN_YEAR = 1400;
    this.MAX_YEAR = 1597;
    this.CENTURIES = {
      1400: "1400",
      1450: "1450",
      1500: "1500",
      1550: "1550",
      1597: "1597"
    };
    this.LESS_CENTURIES = {};
    Object.assign(this.LESS_CENTURIES, this.CENTURIES);
    delete this.LESS_CENTURIES[1450];
    delete this.LESS_CENTURIES[1550];
  },
  setup() {
    const smAndDown = useDisplay();
    return smAndDown;
  },
  methods: {
    updateYearsRange(event) {
      if (event[0] + YEAR_CHRISTMAS !== Number(this.y__year__gte)) {
        this.$emit("update:y__year__gte", event[0] + YEAR_CHRISTMAS);
      }
      if (event[1] + YEAR_CHRISTMAS !== Number(this.y__year__lt)) {
        this.$emit("update:y__year__lt", event[1] + YEAR_CHRISTMAS);
      }
    }
  }
};

</script>

