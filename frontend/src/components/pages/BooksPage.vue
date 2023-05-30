<template>
  {{ books }}
</template>

<script>

export default {
  props: {
    books: {
      type: Object,
      required: true,
    },
  },
};
</script>
