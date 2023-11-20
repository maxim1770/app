<template>
  <div class="mt-2">
    <div class="d-flex justify-space-between align-center mb-2">
      <MainSmallTitle :title="headTitle" />
      <slot name="head"></slot>
    </div>
    <slot></slot>
    <v-divider v-if="hasDivider" />
  </div>
</template>

<script>


import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle },
  props: {
    headTitle: {
      type: String,
      required: true
    },
    hasDivider: {
      type: Boolean,
      required: false,
      default: false
    }
  }
};
</script>