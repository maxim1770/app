<template>
  <div>
    <ManuscriptPage v-if="manuscript?.id" :manuscript="manuscript" />
    <ChapterWithHead headTitle="Другие Рукописи">
      <ManuscriptsView />
    </ChapterWithHead>
  </div>
</template>

<script>
import { api } from "@/services/api";
import ManuscriptPage from "@/components/pages/ManuscriptPage.vue";
import { numObjectKeys, replaceRouterQuery } from "@/utils/common";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ManuscriptsView from "@/views/ManuscriptsView.vue";

export default {
  components: { ManuscriptsView, ChapterWithHead, ManuscriptPage },

  data() {
    return {
      manuscript: {
        type: Object,
        required: true
      }
    };
  },
  watch: {
    $route(to, from) {
      this.getManuscript();
    },
    manuscript() {
      if (!numObjectKeys(this.$route.query)) {
        this.replaceRouterQuery({
          fund__title: this.manuscript.fund?.title,
          fund__library: this.manuscript.fund?.library,
          search: !this.manuscript.fund ? "lls" : null
        });
      }
    }
  },
  mounted() {
    this.getManuscript();
  },
  methods: {
    replaceRouterQuery,
    getManuscript() {
      api
        .getManuscript(this.$route.params.manuscriptCode)
        .then((response) => (this.manuscript = response.data));
    }
  }
};
</script>
