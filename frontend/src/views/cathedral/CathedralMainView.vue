<template>
  <div>
    <CathedralView />
    <ChapterWithHead headTitle="Другие Соборы">
      <CathedralsView />
    </ChapterWithHead>
  </div>
</template>

<script>
import CathedralsView from "@/views/CathedralsView.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import CathedralView from "@/views/cathedral/CathedralView.vue";

export default {
  components: { CathedralView, ChapterWithHead, CathedralsView }

};
</script>
