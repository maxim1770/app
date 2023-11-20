<template>
  <p
    :class="`text-body-1 text-sm-h6 text-md-h5 font-weight-bold ma-2 text-center text-${textColor}`"
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
      default: false
    }
  }
};

</script>

