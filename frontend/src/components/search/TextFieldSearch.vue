<template>
  <v-text-field
    @update:modelValue="$emit('update:search', $event)"
    :model-value="search"
    label="Поиск..."
    variant="solo"
    prepend-inner-icon="mdi-magnify"
    single-line
    clearable
  ></v-text-field>
</template>

<script>


export default {
  props: {
    search: {
      type: String,
      required: true
    }
  },
  emits: ["update:search"]
};

</script>



