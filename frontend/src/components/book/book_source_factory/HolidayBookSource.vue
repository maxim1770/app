<template>
  <div class="mb-5">
    <ChapterWithHead
      v-if="holiday"
      headTitle="Праздник"
    >
      <ListHolidays :holidays="[holiday]" :hasHeadTitle="false" />
    </ChapterWithHead>
    <ChapterSaint
      v-else
      :saint="saint"
      headTitle="Святой"
    />
    <ChapterSaint
      :saint="book?.author"
      headTitle="Автор"
    />
  </div>
</template>

<script>


import ChapterWithHead from "@/components/common/ChapterWithHead.vue";
import ListHolidays from "@/components/holiday/ListHolidays.vue";
import ChapterSaint from "@/components/saint/ChapterSaint.vue";

export default {
  components: { ChapterSaint, ListHolidays, ChapterWithHead },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  computed: {
    holiday() {
      return this.book.holiday_book ? this.book.holiday_book?.holiday : this.book?.molitva_book.holiday;
    },
    saint() {
      return this.book?.holiday_book?.saint;
    }
  }
};

</script>



