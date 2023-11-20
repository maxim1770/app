<template>
  <v-list-item
    v-if="dignity"
    prepend-icon="mdi-menorah-fire"
  >
    Сан
    <BadgeDignity :dignity="dignity" class="ml-1" />
  </v-list-item>
</template>

<script>


import BadgeDignity from "@/components/saint/dignity/BadgeDignity.vue";

export default {
  components: { BadgeDignity },
  props: {
    dignity: {
      type: Object,
      required: true
    }
  }
};

</script>



