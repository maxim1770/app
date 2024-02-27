<template>
  <div
    v-memo="[movableDates?.length]"
  >
    <ImgMainTitle mainPageValue="movable-dates" />
    <MainTitle
      title="Указатель Евангельских и Апостольских чтений на каждый день года"
      textColor="red-accent-4"
      :hasDivider="true"
    />
    <ChapterWithHead>
      <template v-slot:head>
        <UnfoldBtns @openAll="openAll" @closeAll="closeAll" />
      </template>
      <v-list
        v-model:opened="open"
        class="text-center"
      >
        <ListGroupCycle :cycle="sortedMovableDates[0]">
          <Cycle1And2 :cycle="movableDates[0]" />
        </ListGroupCycle>
        <ListGroupCycle :cycle="sortedMovableDates[1]" class="my-7">
          <Cycle1And2 :cycle="sortedMovableDates[1]" />
        </ListGroupCycle>
        <ListGroupCycle :cycle="sortedMovableDates[2]">
          <Cycle3 :cycle="sortedMovableDates[2]" />
        </ListGroupCycle>
      </v-list>
    </ChapterWithHead>
  </div>
</template>

<script>

import Cycle1And2 from "@/components/movable_date/Cycle1And2.vue";
import Cycle3 from "@/components/movable_date/Cycle3.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import HeadBookmarkFullTitleFactory from "@/components/book/HeadBookmarkFullTitleFactory.vue";
import ListGroupCycle from "@/components/movable_date/ListGroupCycle.vue";
import UnfoldBtns from "@/components/common/UnfoldBtns.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";


export default {

  components: {
    ImgMainTitle,
    ChapterWithHead,
    UnfoldBtns,
    ListGroupCycle,
    HeadBookmarkFullTitleFactory,
    BookFullTitleFactory, MainTitle, MainSmallTitle, Cycle1And2, Cycle3
  },
  props: {
    movableDates: {
      type: Array,
      required: true
    }
  },
  data() {
    return {
      open: [1, 2, 3]
    };
  },
  computed: {
    sortedMovableDates() {
      let sortedMovableDates = this.movableDates.sort((cycle_1, cycle_2) => cycle_1.num > cycle_2.num ? 1 : -1);
      for (let cycle of sortedMovableDates) {
        cycle.weeks.sort(
          (week_1, week_2) =>
            week_1.sunday_num > week_2?.sunday_num ? 1 : -1
        );
      }
      return sortedMovableDates;
    }
  },
  methods: {
    openAll() {
      this.open = [1, 2, 3];
    },
    closeAll() {
      this.open = [];
    }
  }
};
</script>

