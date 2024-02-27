<template>
  <v-chip
    v-if="is_solid_week"
    color="amber"
    prepend-icon="mdi-calendar-week"
    class="ma-1"
    :style="{ 'font-size': !lgAndUp ? 'small' : 'medium' }"
  >
    Сплошная седмица
  </v-chip>
</template>

<script>


import { useDisplay } from "vuetify";

export default {
  props: {
    is_solid_week: {
      type: Boolean,
      required: true
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>
