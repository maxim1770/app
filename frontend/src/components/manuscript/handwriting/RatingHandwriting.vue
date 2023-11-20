<template>
  <v-rating
    v-model=v_model_handwriting_to_rating
    empty-icon="mdi-pencil-outline"
    full-icon="mdi-pencil"
    active-color="red-accent-4"
    :disabled="true"
    half-increments
    size="25"
    length="5"
  >
  </v-rating>
</template>

<script>


export default {
  props: {
    handwriting_to_rating: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      v_model_handwriting_to_rating: this.handwriting_to_rating
    };
  }
};

</script>



