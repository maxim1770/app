<template>
    <div>
        <CyclePage :cycle='movableDates[0]'/>
        <CyclePage :cycle='movableDates[1]'/>
    </div>
</template>

<script>

import CyclePage from "@/components/CyclePage.vue";

export default {

  components: {CyclePage},

  props: {
    movableDates: {
      type: Object,
      required: true,
    },
  },
}
</script>

