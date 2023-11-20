<template>
  <v-card>
    <v-card-item>
      <v-list>
        <ListItemsFund :manuscript="manuscript" />
        <ListItemYear :year="manuscript?.year" />
        <ListItemHandwriting :manuscript="manuscript" />
        <ListItemNumBookmarks :manuscript="manuscript" />
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemsFund from "@/components/manuscript/fund/ListItemsFund.vue";
import ListItemHandwriting from "@/components/manuscript/handwriting/ListItemHandwriting.vue";
import ListItemNumBookmarks from "@/components/bookmark/num_bookmarks/ListItemNumBookmarks.vue";

export default {
  components: { ListItemNumBookmarks, ListItemHandwriting, ListItemsFund, ListItemYear },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



