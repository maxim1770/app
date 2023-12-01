<template>
  <v-badge
    v-if="holiday_category"
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






