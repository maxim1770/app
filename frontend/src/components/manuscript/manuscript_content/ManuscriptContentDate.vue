<template>
  <ChapterWithHead
    headTitle="Содержание"
    class="mt-3"
  >
    <template v-slot:head>
      <UnfoldBtns @openAll="openAll" @closeAll="closeAll" />
    </template>
    <v-card>
      <v-card-item>
        <v-list
          v-model:opened="open"
          density="compact"
        >
          <v-list-group
            v-for="days_nums_dict in manuscript?.structured_bookmarks"
            :key="days_nums_dict[0]"
            :value="monthTitle(days_nums_dict[0])"
          >
            <template v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
              >
                <v-chip
                  color="green-lighten-1"
                  class="ma-1"
                >
                  <v-list-item-title>
                    <SmallTitle
                      :title="monthTitle(days_nums_dict[0])"
                      textColor="green-lighten-1"
                    />
                  </v-list-item-title>
                </v-chip>
              </v-list-item>
            </template>
            <v-list-group
              v-for="(bookmarks, day_num, index) in days_nums_dict[1]"
              :key="index"
              :value="day_num"
            >
              <template v-slot:activator="{ props }">
                <v-list-item
                  v-bind="props"
                >
                  <v-list-item-title>
                    <SmallTitle
                      :title="day_num"
                      textColor="green-lighten-2"
                    />
                  </v-list-item-title>
                </v-list-item>
              </template>
              <v-list-item
                v-for="bookmark in bookmarks"
                :key="bookmark.book.id"
                :to="{ name: 'book', params: { bookId: bookmark.book?.id } }"
              >
                <BookFullTitleFactory :book="bookmark?.book" />
              </v-list-item>
            </v-list-group>
          </v-list-group>
        </v-list>
      </v-card-item>
    </v-card>
  </ChapterWithHead>
</template>

<script>


import BookFullTitleFactory from "@/components/book/book_full_title/BookFullTitleFactory.vue";
import { MONTH_TITLE } from "@/utils/common";
import UnfoldBtns from "@/components/common/UnfoldBtns.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";
import ChipChapter from "@/components/manuscript/ChipChapter.vue";
import SmallTitle from "@/components/common/title/SmallTitle.vue";

export default {
  components: {
    SmallTitle,
    ChipChapter,
    MainSmallTitle,
    ChapterWithHead,
    UnfoldBtns,
    BookFullTitleFactory
  },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      open: []
    };
  },
  methods: {
    monthTitle(monthNum) {
      return MONTH_TITLE[monthNum];
    },
    openAll() {
      this.open = Object.values(MONTH_TITLE);
      for (let i = 0; i < 31; i++) {
        this.open.push(i.toString());
      }

    },
    closeAll() {
      this.open = [];
    }
  }
};

</script>

