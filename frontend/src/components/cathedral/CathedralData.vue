<template>
  <v-card>
    <v-card-item>
      <v-list>
        <ListItemYear :year="cathedral?.year" />
        <ListItemNumSaints :cathedral="cathedral" />
        <ListItemNumRules :cathedral="cathedral" />
      </v-list>
    </v-card-item>
  </v-card>
</template>

<script>


import ListItemYear from "@/components/year/ListItemYear.vue";
import ListItemNumRules from "@/components/cathedral/ListItemNumRules.vue";
import ListItemNumSaints from "@/components/cathedral/ListItemNumSaints.vue";

export default {
  components: { ListItemNumSaints, ListItemNumRules, ListItemYear },
  props: {
    cathedral: {
      type: Object,
      required: true
    }
  }
};

</script>



