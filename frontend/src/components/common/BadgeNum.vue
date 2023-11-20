<template>
  <v-badge
    :content="num"
    :color="color"
  />
</template>


<script>


export default {
  props: {
    num: {
      type: Number,
      required: true
    },
    color: {
      type: String,
      required: false,
      default: "blue"
    }
  }
};

</script>



