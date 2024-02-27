<template>
  <v-navigation-drawer
    :model-value="drawer"
    @update:modelValue="$emit('update:drawer', $event)"
    width="300"
  >
    <NavigationDrawerPrepend v-once />
    <v-divider />
    <NavigationDrawerHoliday :mainData="mainData" />
    <v-divider />
    <NavigationDrawerList v-once />
    <v-divider />
    <NavigationDrawerRandomBook v-once />
    <v-divider />
    <NavigationDrawerLink v-once />
    <v-divider />
    <NavigationDrawerShare v-once />
  </v-navigation-drawer>
</template>

<script>


import NavigationDrawerPrepend from "@/components/app/app_bar/navigation_drawer/NavigationDrawerPrepend.vue";
import NavigationDrawerList from "@/components/app/app_bar/navigation_drawer/NavigationDrawerList.vue";
import NavigationDrawerRandomBook from "@/components/book/random_book/NavigationDrawerRandomBook.vue";
import NavigationDrawerHoliday from "@/components/holiday/NavigationDrawerHoliday.vue";
import NavigationDrawerLink from "@/components/app/app_bar/navigation_drawer/NavigationDrawerLink.vue";
import NavigationDrawerShare from "@/components/app/app_bar/navigation_drawer/NavigationDrawerShare.vue";

export default {
  components: {
    NavigationDrawerShare,
    NavigationDrawerLink,
    NavigationDrawerHoliday,
    NavigationDrawerRandomBook,
    NavigationDrawerList,
    NavigationDrawerPrepend
  },
  props: {
    drawer: {
      type: Boolean,
      required: true
    },
    mainData: {
      type: Object,
      required: true
    }
  },
  emits: [
    "update:drawer"
  ]
};

</script>



