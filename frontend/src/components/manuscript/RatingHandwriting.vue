<template>
  <!--  <v-rating-->
  <!--    v-model=manuscript?.handwriting_to_rating-->
  <!--    empty-icon="mdi-pencil-outline"-->
  <!--    full-icon="mdi-pencil"-->
  <!--    active-color="red-accent-4"-->
  <!--    half-increments-->
  <!--    size="25"-->
  <!--    length="5"-->
  <!--  ></v-rating>-->
  {{ manuscript?.handwriting_to_rating }}
</template>

<script>


export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



