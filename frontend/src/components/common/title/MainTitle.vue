<template>
  <p
    class="text-h6 text-sm-h5 text-md-h4 font-weight-bold text-center"
    :class="[hasMargin ? 'ma-2' : '', `text-${textColor}`]"
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
    },
    hasMargin: {
      type: Boolean,
      required: false,
      default: true
    }
  }
};

</script>

