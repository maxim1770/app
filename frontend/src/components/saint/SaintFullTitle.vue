<template>
  {{ saint.name }}
  <ChipFaceSanctity v-if="saint.face_sanctity" :face_sanctity="saint.face_sanctity" class="ml-1" />
  <ChipDignity v-if="saint.dignity" :dignity="saint.dignity" class="ml-1" />
</template>

<script>


import ChipDignity from "@/components/saint/ChipDignity.vue";
import ChipFaceSanctity from "@/components/saint/ChipFaceSanctity.vue";

export default {
  components: { ChipFaceSanctity, ChipDignity },
  props: {
    saint: {
      type: Object,
      required: true
    }
  }
};

</script>



