<template>
  <div class="my-2">
    <v-sheet class="bg-blue-lighten-2 pa-12" rounded>
      <v-card class="mx-auto px-6 py-8" max-width="500">
        <div>
          <v-combobox
            v-model="preview_page_in_num"
            label="Num"
            variant="underlined"
            clearable
            class="mb-2"
          ></v-combobox>
          <br>
          <v-select
            v-model="preview_page_in_position"
            :items="[0, 1]"
            label="Position"
            variant="underlined"
            clearable
            class="mb-2"
          ></v-select>
          <br>
          <v-btn
            @click="putManuscript"
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

export default {
  props: {
    manuscript: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      preview_page_in_num: null,
      preview_page_in_position: null
    };
  },
  computed: {
    preview_page_in() {
      return { "num": Number(this.preview_page_in_num), "position": Number(this.preview_page_in_position) };
    }
  },
  methods: {
    putManuscript() {
      api
        .putManuscript({
          "manuscriptCode": this.$route.params.manuscriptCode,
          "preview_page_in": this.preview_page_in
        })
        .then((response) => (this.manuscript = response.data));
    }
  }
};

</script>



