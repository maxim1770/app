<template>
  <p
    :class="`text-h5 text-sm-h4 text-md-h3 font-weight-bold ma-2 text-center text-${textColor}`"
  >
    {{ title }}
  </p>
  <v-divider v-if="hasDivider" />
</template>

<script>


export default {
  props: {
    title: {
      type: String,
      required: true
    },
    textColor: {
      type: String,
      required: false,
      default: "black"
    },
    hasDivider: {
      type: Boolean,
      required: false,
      default: true
    }
  }
};

</script>

