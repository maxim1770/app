<template>
  <v-badge
    v-if="dignity"
    :content="dignity?.title"
    color="blue"
  />
</template>

<script>


export default {
  props: {
    dignity: {
      type: Object,
      required: true
    }
  }
};

</script>



