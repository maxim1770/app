<template>
  <div class="d-flex justify-space-between ma-3 mt-5">
    <p>Всего</p>
    <BadgeNum :num="numItems" />
  </div>
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";

export default {
  components: { BadgeNum },
  props: {
    numItems: {
      type: Number,
      required: true
    }
  }
};

</script>



