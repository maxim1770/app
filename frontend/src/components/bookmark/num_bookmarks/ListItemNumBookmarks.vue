<template>
  <v-list-item
    v-if="manuscript.num_bookmarks"
    prepend-icon="mdi-book-outline"
  >
    Количество закладок
    <ChipNumBookmarks :manuscript="manuscript" class="ma-1" />
  </v-list-item>
</template>

<script>


import ChipNumBookmarks from "@/components/bookmark/num_bookmarks/ChipNumBookmarks.vue";

export default {
  components: { ChipNumBookmarks },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>






