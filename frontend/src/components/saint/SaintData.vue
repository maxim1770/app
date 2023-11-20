<template>
  <v-card
    v-if="saint?.dignity || saint?.face_sanctity"
  >
    <v-card-item>
      <v-list>
        <ListItemDignity :dignity="saint.dignity" />
        <ListItemFaceSanctity :face_sanctity="saint.face_sanctity" />
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import ListItemFaceSanctity from "@/components/saint/face_sanctity/ListItemFaceSanctity.vue";
import ListItemDignity from "@/components/saint/dignity/ListItemDignity.vue";


export default {
  components: { ListItemDignity, ListItemFaceSanctity },
  props: {
    saint: {
      type: Object,
      required: true
    }
  }
};

</script>



