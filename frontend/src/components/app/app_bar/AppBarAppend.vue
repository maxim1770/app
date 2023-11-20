<template v-slot:append>
  <!--      <v-combobox-->
  <!--      label="Поиск..."-->
  <!--      clearable-->
  <!--      hide-details-->
  <!--      prepend-icon="mdi-magnify"-->
  <!--      single-line-->
  <!--      style="min-width: 200px"-->
  <!--      @click:prepend=""-->
  <!--    ></v-combobox>-->
  <v-divider
    class="mx-2"
    vertical
  />
  <AppBarDate :date="mainData.date" />
  <v-divider
    class="mx-2"
    vertical
  />
  <v-app-bar-nav-icon
    @click.stop="$emit('update:drawer', $event)"
    variant="text"
  />
</template>

<script>


import { useDisplay } from "vuetify";
import AppBarDate from "@/components/date/AppBarDate.vue";

export default {
  components: { AppBarDate },
  props: {
    mainData: {
      type: Object,
      required: true
    }
  },
  emits: [
    "update:drawer"
  ],
  setup() {
    const lgAndUp = useDisplay();
    return lgAndUp;
  }
};

</script>



