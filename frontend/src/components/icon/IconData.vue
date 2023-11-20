<template>
  <v-card>
    <v-card-item>
      <v-list>
        <ListItemIconLibrary :icon="icon" />
        <ListItemYear :year="icon?.year" />
        <ListItemCity :city="icon?.city" />
        <ListItemDownload :path="icon.path" />
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemCity from "@/components/city/ListItemCity.vue";
import ListItemIconLibrary from "@/components/city/ListItemIconLibrary.vue";
import ListItemDownload from "@/components/common/download/ListItemDownload.vue";

export default {
  components: { ListItemDownload, ListItemIconLibrary, ListItemYear, ListItemCity },
  props: {
    icon: {
      type: Object,
      required: true
    }
  }

};

</script>



