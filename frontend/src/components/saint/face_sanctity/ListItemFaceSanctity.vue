<template>
  <v-list-item
    v-if="face_sanctity"
    prepend-icon="mdi-book-open-variant"
  >
    Лик Святости
    <BadgeFaceSanctity :face_sanctity="face_sanctity" class="ml-1" />
  </v-list-item>
</template>

<script>


import BadgeFaceSanctity from "@/components/saint/face_sanctity/BadgeFaceSanctity.vue";

export default {
  components: { BadgeFaceSanctity },
  props: {
    face_sanctity: {
      type: Object,
      required: true
    }
  }
};

</script>



