<template>
  <v-badge
    v-if="dignity"
    @click="$router.push({ name: 'saints', query: {dignity__title: dignity?.title} })"
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



