<template>
  <div
    v-memo="[icon?.id]"
  >
    <GalleryMain :imgs_paths="[this.icon?.path]" :has_preview_img="false" :has_cover="false" />
    <MainSmallTitle :title="icon.desc" />
    <IconData :icon="icon" />
    <ListHolidays :holidays="holidays" />
  </div>
</template>


<script>

import ListHolidays from "@/components/holiday/ListHolidays.vue";
import IconData from "@/components/icon/IconData.vue";
import GalleryMain from "@/components/gallery/GalleryMain.vue";
import MainSmallTitle from "@/components/common/title/MainSmallTitle.vue";

export default {
  components: { MainSmallTitle, GalleryMain, IconData, ListHolidays },
  props: {
    icon: {
      type: Object,
      required: true
    }
  },
  computed: {
    holidays() {
      const holidays = [];
      for (let i in this.icon.holidays) {
        holidays.push(this.icon.holidays[i]?.holiday);
      }
      return holidays;
    }
  }
};
</script>



