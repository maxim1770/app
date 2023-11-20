<!--:style="{ 'height': xlAndUp ? '450px' : '250px' }" было раньше в /books-->
<template>
  <v-img
    :src="src"
    style="width: 100%;"
    :style="{ 'max-height': lgAndUp ? '650px' : '450px' }"
    :cover="has_cover"
    class="rounded-xl"
  >
    <template v-slot:placeholder>
      <div class="d-flex align-center justify-center fill-height">
        <v-progress-circular
          color="grey-lighten-4"
          indeterminate
        ></v-progress-circular>
      </div>
    </template>
    <div class="d-flex flex-column fill-height justify-center align-center">
      <slot></slot>
    </div>
  </v-img>
</template>

<script>

import { useDisplay } from "vuetify";

export default {
  props: {
    src: {
      type: String,
      required: true
    },
    has_cover: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>

