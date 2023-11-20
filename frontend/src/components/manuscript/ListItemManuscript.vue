<template>
  <v-list-item
    v-if="manuscript?.code"
    :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
    prepend-icon="mdi-bookshelf"
    class="mt-1"
  >
    <ManuscriptFullTitle :manuscript="manuscript" />
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



