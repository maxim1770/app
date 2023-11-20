<template>
  <v-badge
    v-if="face_sanctity"
    :content="face_sanctity?.title"
    color="green"
  />
</template>

<script>


export default {
  props: {
    face_sanctity: {
      type: Object,
      required: true
    }
  }
};

</script>



