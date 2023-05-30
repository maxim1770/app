<template>
  <!--  <v-chip class="ml-1">-->
  <!--    {{ molitva_book.title }}-->
  <!--  </v-chip>-->
  <v-chip>
    {{ book }}
  </v-chip>
</template>

<script>


export default {
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>



