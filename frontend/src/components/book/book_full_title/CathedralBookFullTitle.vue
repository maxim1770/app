<template>
  <v-chip>
    Правило
    <v-chip
      variant="tonal"
      color="blue"
      class="ml-1"
    >
      {{ book.cathedral_book.rule_num }}
    </v-chip>
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
