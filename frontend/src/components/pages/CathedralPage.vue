<template>
  <div>
    <ImgMainTitle
      mainPageValue="cathedrals"
      @click="$router.push({ name: 'cathedral', params: { cathedralSlug: cathedral.slug } })"
      :title="cathedral.title"
      :textColor="isVselenskijSobor(cathedral) ? 'red-darken-4' : 'white'"
    />
    <CathedralData :cathedral="cathedral" />
    <ChapterWithHead headTitle="Правила">
      <v-card>
        <v-card-item>
          <ChipGroupNums :some_books="cathedral?.cathedral_books" />
        </v-card-item>
      </v-card>
    </ChapterWithHead>
    <ChapterWithHead headTitle="Рукописи">
      <ContainerManuscripts :manuscripts="cathedral?.manuscripts" />
    </ChapterWithHead>
  </div>

</template>

<script>


import ChipGroupNums from "@/components/common/ChipGroupNums.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ContainerManuscripts from "@/components/manuscript/manuscripts/ContainerManuscripts.vue";
import CathedralData from "@/components/cathedral/CathedralData.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import { isVselenskijSobor } from "@/utils/common";

export default {
  components: { ImgMainTitle, CathedralData, ChapterWithHead, ChipGroupNums, ContainerManuscripts },
  props: {
    cathedral: {
      type: Object,
      required: true
    }
  },
  methods: { isVselenskijSobor }
};
</script>




