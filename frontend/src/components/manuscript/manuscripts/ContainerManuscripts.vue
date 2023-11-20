<template>
  <v-container>
    <v-row
      v-for="i in this.manuscripts?.length"
      :key="i"
    >
      <template v-if="i % 2 === 1">
        <v-col
          v-for="manuscript in this.manuscripts.slice(i-1, i +1)"
          :key="manuscript.id"
          @click="$router.push({name: 'manuscript', params: { manuscriptCode: manuscript.code } })"
          cols="12"
          sm="12"
          :lg="6 ? this.manuscripts?.length > 1 : 12"
          align="center"
        >
          <v-card>
            <ImgWithPlaceholder
              :src="imgUrl(manuscript.preview_page_path)"
              :style="{ 'height': xlAndUp ? '450px' : '250px' }"
            />
            <v-card-item>
              <ManuscriptFullTitle :manuscript="manuscript" />
            </v-card-item>
          </v-card>
        </v-col>
      </template>
    </v-row>
  </v-container>
</template>

<script>


import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import ImgWithPlaceholder from "@/components/gallery/ImgWithPlaceholder.vue";
import { imgUrl } from "@/utils/common";
import { useDisplay } from "vuetify";

export default {
  components: {
    ImgWithPlaceholder,
    ManuscriptFullTitle
  },
  props: {
    manuscripts: {
      type: Array,
      required: true
    }
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  methods: { imgUrl }
};
</script>



