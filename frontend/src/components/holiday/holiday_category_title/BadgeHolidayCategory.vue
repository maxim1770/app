<template>
  <v-badge
    v-if="holiday_category"
    @click="$router.push({ name: 'holidays', query: {holiday_category__title: holiday_category?.title} })"
    :content="holiday_category?.title"
    color="green-lighten-1"
  />
</template>

<script>


export default {
  props: {
    holiday_category: {
      type: Object,
      required: true
    }
  }
};

</script>


