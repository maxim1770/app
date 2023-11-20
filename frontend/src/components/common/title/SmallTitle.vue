<template>
  <p
    :class="`text-body-2 text-sm-body-1 text-md-h6 font-weight-bold text-${textColor}`"
  >
    {{ title }}
  </p>
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
    }
  }
};

</script>

