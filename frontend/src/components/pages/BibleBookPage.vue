<template>
  <div>
    <ImgMainTitle
      mainPageValue="bible-books"
      @click="$router.push({ name: 'bible-book', params: { bibleBookAbbr: bible_book.abbr } })"
      :title="bible_book.title"
    />
    <ChapterWithHead
      v-if="sorted_some_books?.length"
      :headTitle="bible_book.zachalos?.length ? 'Зачала' : 'Псалмы'"
    >
      <v-card>
        <v-card-item>
          <ChipGroupNums :some_books="sorted_some_books" />
        </v-card-item>
      </v-card>
    </ChapterWithHead>
    <ChapterSaint
      :saint="bible_book.author"
      headTitle="Автор"
    />
    <ChapterWithHead headTitle="Рукописи">
      <ContainerManuscripts :manuscripts="bible_book.manuscripts" />
    </ChapterWithHead>
  </div>
</template>

<script>


import ContainerManuscripts from "@/components/manuscript/manuscripts/ContainerManuscripts.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ChipGroupNums from "@/components/common/ChipGroupNums.vue";
import ImgMainTitle from "@/components/common/ImgMainTitle.vue";
import ChapterSaint from "@/components/saint/ChapterSaint.vue";

export default {
  components: { ChapterSaint, ImgMainTitle, ChipGroupNums, ChapterWithHead, ContainerManuscripts },
  props: {
    bible_book: {
      type: Object,
      required: true
    }
  },
  computed: {
    sorted_some_books() {
      return Object.values(this.__some_books || [])
        .filter(some_book => !some_book.book.title.includes("толк"))
        .sort((some_book_1, some_book_2) => some_book_1.num > some_book_2.num ? 1 : -1);
    },
    __some_books() {
      return this.bible_book.zachalos?.length ? this.bible_book.zachalos : this.bible_book.psaltyr_books;
    }
  }
};
</script>
