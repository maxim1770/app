<template>
  <v-app-bar-title>
    <v-btn
      v-if="lgAndUp"
      :to="{ name: 'main' }"
      variant="tonal"
      rounded="pill"
      size="large"
      color="blue-lighten-1"
      class="text-none"
    >
      <template v-slot:prepend>
        <v-icon
          icon="custom:OrthodoxCross"
          size="x-large"
        />
      </template>
      Православие в Рукописях
    </v-btn>
    <v-btn
      v-else
      :to="{ name: 'main' }"
      variant="tonal"
      rounded="pill"
      size="x-large"
      color="blue-lighten-1"
    >
      <v-icon
        icon="custom:OrthodoxCross"
        size="x-large"
      />
    </v-btn>
  </v-app-bar-title>
</template>

<script>


import { useDisplay } from "vuetify";

export default {
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>



