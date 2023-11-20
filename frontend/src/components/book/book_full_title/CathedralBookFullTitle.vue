<template>
  <router-link
    :to="{ name: 'cathedral', params: { cathedralSlug: cathedral_book.cathedral.slug } }"
    :class="isVselenskijSobor(cathedral_book.cathedral) ? 'text-red-darken-4' : 'text-black'"
    class="text-decoration-none ma-1"
  >
    {{ cathedral_book.cathedral.title }}
  </router-link>
  <ChipYear
    :year="cathedral_book.cathedral.year"
    class="ma-1"
  />
  <v-chip
    color="red-lighten-1"
    class="ma-1"
  >
    Правило
    <BadgeNum
      :num="cathedral_book.rule_num"
      color="red-darken-3"
      class="ml-1"
    />
  </v-chip>
</template>

<script>


import BadgeNum from "@/components/common/BadgeNum.vue";
import ChipYear from "@/components/year/ChipYear.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import { isVselenskijSobor } from "@/utils/common";

export default {
  components: { ImgMainTitle, ChipYear, BadgeNum },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    cathedral_book() {
      return this.book.cathedral_book;
    }
  },
  methods: { isVselenskijSobor }
};

</script>
