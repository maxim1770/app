<template>
  <p class="text-h4 font-weight-bold mr-1">
    {{ saint.name }}
    <v-chip v-if="saint.face_sanctity" class="ma-2" color="green">
      {{ saint.face_sanctity.title }}
    </v-chip>
    <v-chip v-if="saint.dignity" class="ma-2" color="blue">
      {{ saint.dignity.title }}
    </v-chip>
  </p>
</template>

<script>
export default {
  props: {
    saint: {
      type: Object,
      required: true,
    },
  },
};
</script>
