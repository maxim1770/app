<template>
  <div
    v-memo="[cathedrals?.length]"
  >
    <v-divider />
    <v-timeline side="end" align="start">
      <v-timeline-item
        v-for="cathedral in cathedrals"
        :key="cathedral.id"
        @click="$router.push({name: 'cathedral', params: { cathedralSlug: cathedral.slug } })"
        :dot-color="isVselenskijSobor(cathedral) ? 'red-darken-4' : 'red-lighten-2'"
        :size="isVselenskijSobor(cathedral) ? 'default' : 'small'"
        icon="mdi-book-open-page-variant"
        fill-dot
      >
        <template v-if="mdAndUp" v-slot:opposite>
          <ChipYear :year="cathedral.year" />
        </template>
        <CathedralFullTitleByCathedral
          :cathedral="cathedral"
          :has_show_year="!mdAndUp"
        />
      </v-timeline-item>
    </v-timeline>
    <v-divider />
  </div>
</template>

<script>


import ChipYear from "@/components/year/ChipYear.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import { useDisplay } from "vuetify";
import BadgeNum from "@/components/common/BadgeNum.vue";
import CathedralFullTitleByCathedral from "@/components/cathedral/CathedralFullTitle.vue";
import { isVselenskijSobor } from "@/utils/common";

export default {
  components: { CathedralFullTitleByCathedral, BadgeNum, MainTitle, ChipYear },
  props: {
    cathedrals: {
      type: Object,
      required: true
    }
  },
  setup() {
    const mdAndUp = useDisplay();
    return mdAndUp;
  },
  methods: {
    isVselenskijSobor
  }
};
</script>
