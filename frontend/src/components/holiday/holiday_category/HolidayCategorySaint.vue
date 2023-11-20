<template>
  <ChapterSaint
    :saint="holiday.saints[0]"
    :holiday="holiday"
    headTitle="Подробнее"
  />
</template>

<script>


import ChapterSaint from "@/components/saint/ChapterSaint.vue";

export default {
  components: {
    ChapterSaint
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>



