<template>
  <div
    v-if="book?.author"
    class="mb-5"
  >
    <ChapterSaint
      :saint="book?.author"
      headTitle="Автор"
    />
  </div>
</template>

<script>


import ChapterSaint from "@/components/saint/ChapterSaint.vue";

export default {
  components: { ChapterSaint },
  props: {
    book: {
      type: Object,
      required: true
    }
  }
};

</script>



