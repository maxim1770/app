<template>
  <div>
    <CarouselMain :imgs_data="holiday?.icons" :has_cover="false" />
    <MainTitle :title="holiday?.title" :textColor="choiceHolidayColor(holiday)" />
    <!--    <AdminSelectHolidayTipikon :holiday="holiday" />-->
    <HolidayFactory :holiday="holiday" />
    <BooksForHoliday
      :molitva_books_by_manuscript="holiday?.molitva_books_by_manuscript"
      :holiday_books="holiday?.holiday_books"
      :holiday="holiday"
    />
  </div>
</template>


<script>

import { choiceHolidayColor, isGreatHoliday } from "@/utils/holidays";
import HolidayFactory from "@/components/holiday/holiday/HolidayFactory.vue";
import AdminSelectHolidayTipikon from "@/components/holiday/AdminSelectHolidayTipikon.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";
import BooksForHoliday from "@/components/book/book_for_holiday/BooksForHoliday.vue";
import CarouselMain from "@/components/gallery/CarouselMain.vue";
import ChapterWithHead from "@/components/common/ChapterWithHead.vue";


export default {
  components: {
    ChapterWithHead,
    CarouselMain,
    BooksForHoliday,
    MainTitle,
    HolidayFactory,
    AdminSelectHolidayTipikon
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  },
  computed: {
    isGreatHoliday() {
      return isGreatHoliday(this.holiday?.holiday_category.title);
    }
  },
  setup() {
    // const theme = useTheme();
    // return { theme };
  },
  mounted() {
    // if (this.isGreatHoliday) {
    //   this.theme.global.name.value = "myCustomLightTheme";
    // }
  },
  methods: { choiceHolidayColor }

};
</script>


