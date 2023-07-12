<template>
  <v-timeline align="start">
    <v-timeline-item
      v-for="bible_book in bible_books"
      :key="bible_book.id"
      dot-color="blue"
      size="small"
    >
      <div class="d-flex">
        <div>
          <strong>{{ bible_book.title }}</strong>
          <v-menu v-if="bible_book.manuscripts?.length" activator="parent" transition="scale-transition" open-on-hover>
            <v-sheet elevation="8" rounded="lg">
              <h3 class="ma-3 ">Рукописи:</h3>
              <v-divider></v-divider>
              <v-list class="ma-1">
                <v-list-item
                  v-for="manuscript in bible_book.manuscripts"
                  :key="manuscript.id"
                  :to="{ name: 'manuscript', params: { manuscriptCode: manuscript.code } }"
                  rounded="xl"
                >
                  <ManuscriptFullTitle :manuscript="manuscript" />
                </v-list-item>
              </v-list>
            </v-sheet>
          </v-menu>
        </div>
      </div>
    </v-timeline-item>
  </v-timeline>
</template>

<script>


import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";

export default {
  components: { ManuscriptFullTitle },
  props: {
    bible_books: {
      type: Object,
      required: true
    }
  }
};

</script>



