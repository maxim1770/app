<template>
  <v-badge
    :content="`${bookmark?.num_pages} л.`"
    color="green-lighten-1"
    inline
  />
</template>

<script>


export default {
  props: {
    bookmark: {
      type: Object,
      required: true
    }
  }
};

</script>



