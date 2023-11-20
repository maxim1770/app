<template>
  <v-btn-toggle
    variant="outlined"
    rounded="lg"
    divided
  >
    <v-btn size="x-small" icon="mdi-unfold-more-horizontal" @click="$emit('openAll')"></v-btn>
    <v-btn size="x-small" icon="mdi-unfold-less-horizontal" @click="$emit('closeAll')"></v-btn>
  </v-btn-toggle>

</template>

<script>


export default {
  emits: ["openAll", "closeAll"]
};

</script>



