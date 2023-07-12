<template>
  <v-list-item
    :prepend-icon="`custom:${tipikon.title_en.replace('_', '')}`"
  >
    Типикон Праздника:
    <ChipTipikon :tipikon="tipikon" class="ml-1" />
  </v-list-item>
</template>

<script>


import ChipTipikon from "@/components/tipikon/ChipTipikon.vue";

export default {
  components: { ChipTipikon },
  props: {
    tipikon: {
      type: Object,
      required: true
    }
  }

};

</script>


