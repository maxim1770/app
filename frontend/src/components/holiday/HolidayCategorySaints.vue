<template>
  <div class="mt-2">
    <h3>Святые:</h3>
    <v-list>
      <v-list-item
        v-for="saint in holiday.saints"
        :key="saint.id"
        :title="saint.name"
        :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
        linec="two"
        rounded="xl"
        class="my-1"
      >
        <ChipFaceSanctity v-if="saint.face_sanctity" :face_sanctity="saint.face_sanctity" />
        <ChipDignity v-if="saint.dignity" :dignity="saint.dignity" class="ml-1" />
      </v-list-item>
    </v-list>
  </div>
</template>

<script>

import ChipFaceSanctity from "@/components/saint/ChipFaceSanctity.vue";
import ChipDignity from "@/components/saint/ChipDignity.vue";

export default {
  components: { ChipFaceSanctity, ChipDignity },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>

