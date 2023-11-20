<template>
  <v-chip
    v-if="year"
    color="blue"
    prepend-icon="mdi-timer-sand"
  >
    <template
      v-if="title"
    >
      {{ title }}
    </template>
    {{ year.title }}
  </v-chip>
</template>

<script>


export default {
  props: {
    year: {
      type: Object,
      required: true
    },
    title: {
      type: String,
      required: false,
      default: null
    }
  }
};

</script>



