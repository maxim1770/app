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
    vertical
    class="mx-2"
  />
  <AppBarDate
    v-memo="[mainData.date?.day?.id]"
    :date="mainData.date"
  />
  <v-divider
    vertical
    class="mx-2"
  />
  <v-app-bar-nav-icon
    v-once
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



