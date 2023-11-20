<template>
  <div class="my-2">
    <v-sheet class="bg-blue-lighten-2 pa-12" rounded>
      <v-card class="mx-auto px-6 py-8" max-width="500">
        <div>
          <v-autocomplete
            v-model="manuscriptCode"
            label="Manuscript Code"
            :items="manuscriptsCodes"
            variant="underlined"
            clearable
          ></v-autocomplete>
          <br>
          First Page
          <PageForm v-model:page="first_page" />
          <br>
          End Page
          <PageForm v-model:page="end_page" />
          <br>
          <v-btn
            @click="putBookmarkPages"
            block
            color="success"
            size="large"
            type="submit"
            variant="elevated"
          >
            Обновить
          </v-btn>
        </div>
      </v-card>
    </v-sheet>
    <v-divider />
  </div>
</template>

<script>


import { api } from "@/services/api";
import PageForm from "@/components/page/PageForm.vue";

export default {
  components: { PageForm },
  props: {
    book: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      manuscriptCode: null,
      first_page: null,
      end_page: null
    };
  },
  computed: {
    manuscriptsCodes() {
      let manuscriptsCodes = [];
      for (let bookmark of this.book.bookmarks) {
        manuscriptsCodes.push(bookmark.manuscript.code);
      }
      return manuscriptsCodes;
    },
    pages_in() {
      return {
        "first_page": this.first_page,
        "end_page": this.end_page
      };
    }
  },
  methods: {
    putBookmarkPages() {
      api
        .putBookmarkPages({
          "bookId": this.$route.params.bookId,
          "manuscriptCode": this.manuscriptCode,
          "pages_in": this.pages_in
        })
        .then((response) => (this.book = response.data));
    }
  }
};

</script>



