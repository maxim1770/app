<template>
  <v-badge
    :content="post?.title || 'Поста нет'"
    color="blue"
  />
</template>

<script>


export default {
  props: {
    post: {
      type: Object,
      required: true
    }
  }
};

</script>
