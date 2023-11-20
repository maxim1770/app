<template>
  <div>
    <SaintPage v-if="saint.id" :saint="saint" />
    <ChapterWithHead headTitle="Другие Святые">
      <SaintsView />
    </ChapterWithHead>
  </div>
</template>

<script>
import { api } from "@/services/api";
import SaintPage from "@/components/pages/SaintPage.vue";
import { numObjectKeys, replaceRouterQuery } from "@/utils/common";
import SaintsView from "@/views/SaintsView.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";

export default {
  components: { ChapterWithHead, SaintsView, SaintPage },

  data() {
    return {
      saint: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getSaint();
    },
    saint() {
      if (!numObjectKeys(this.$route.query)) {
        this.replaceRouterQuery({
          face_sanctity__title: this.saint.face_sanctity?.title,
          dignity__title: this.saint.dignity?.title
        });
      }
    }
  },
  mounted() {
    this.getSaint();
  },
  methods: {
    replaceRouterQuery,
    getSaint() {
      api
        .getSaint(this.$route.params.saintSlug)
        .then((response) => (this.saint = response.data));
    }
  }

};
</script>
