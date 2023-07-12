<template>
  <v-timeline align="start">
    <v-timeline-item
      v-for="manuscript in llsManuscripts"
      :key="manuscript.id"
      dot-color="blue"
      size="small"
    >
      <router-link
        v-if="manuscript.code"
        :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
      >
        <strong>{{ manuscript.title }}</strong>
        <div class="text-caption">
          Рукопись взята с сайта "Руниверс" {{ manuscript.url }}
        </div>
      </router-link>
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";

export default {
  components: { ManuscriptFullTitle },
  props: {
    llsManuscripts: {
      type: Object,
      required: true
    }
  }
};

</script>



