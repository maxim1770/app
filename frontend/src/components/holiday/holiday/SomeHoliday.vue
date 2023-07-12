<template>
  <v-list lines="one">
    <ListItemTipikon v-if="holiday?.tipikon" :tipikon="holiday.tipikon" />
    <ListItemDay v-if="holiday?.day" :day="holiday.day" />
    <ListItemMovableDay v-else :movable_day="holiday?.movable_day" />
    <ListItemYear v-if="holiday?.year" :year="holiday.year" />
  </v-list>
  <v-divider></v-divider>
  <HolidayCategoryFactory v-if="holiday?.saints.length" :holiday="holiday" />
  <v-divider></v-divider>
</template>

<script>


import HolidayCategoryFactory from "@/components/holiday/holiday_category/HolidayCategoryFactory.vue";
import ListItemDay from "@/components/day/ListItemDay.vue";
import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemMovableDay from "@/components/movable_day/ListItemMovableDay.vue";
import ListItemTipikon from "@/components/tipikon/ListItemTipikon.vue";

export default {
  components: {
    ListItemTipikon,
    HolidayCategoryFactory,
    ListItemDay,
    ListItemMovableDay,
    ListItemYear
  },
  props: {
    holiday: {
      type: Object,
      required: true
    }
  }
};

</script>



