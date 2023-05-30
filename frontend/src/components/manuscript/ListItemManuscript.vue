<template>
  <v-list-item v-if="manuscript?.code" prepend-icon="mdi-bookshelf">
    Источник:
    <v-chip
      :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
      class="ml-1"
    >
      <ManuscriptFullTitle :manuscript="manuscript" />
    </v-chip>
  </v-list-item>
</template>

<script>


import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";

export default {
  components: { ManuscriptFullTitle },
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  }
};

</script>



