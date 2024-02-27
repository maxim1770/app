<template>
  <v-badge
    v-if="face_sanctity"
    @click="$router.push({ name: 'saints', query: {face_sanctity__title: face_sanctity?.title} })"
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



