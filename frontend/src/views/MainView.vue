<template>
  <div>
    <v-container>
      <v-row
        v-for="i in this.mainPages?.length"
        :key="i"
      >
        <template v-if="i % 2 === 1">
          <v-col
            v-for="mainPage in this.mainPages.slice(i-1, i +1)"
            :key="mainPage.values"
            @click="$router.push({name: mainPage.value})"
            cols="12"
            sm="12"
            :lg="6 ? this.mainPages?.length > 1 : 12"
            align="center"
          >
            <v-card>
              <ImgWithPlaceholder
                :src="imgUrl(mainPage.img)"
                :style="{ 'height': xlAndUp ? '450px' : '250px' }"
              >
                <MainTitle :title="mainPage.title" textColor="white" />
              </ImgWithPlaceholder>
            </v-card>
          </v-col>
        </template>
      </v-row>
    </v-container>
    <v-divider class="my-5" />
    <DatePage
      v-if="mainData.date?.year"
      :date="mainData.date"
    />
  </div>
  <!--  <div>-->
  <!--    <v-btn-group>-->
  <!--      <v-btn-->
  <!--        @click="$router.push({ name: 'lls'})"-->
  <!--      >-->
  <!--        lls-->
  <!--      </v-btn>-->
  <!--      <v-btn-->
  <!--        @click="$router.push({ name: 'bible-books'})"-->
  <!--      >-->
  <!--        bible-books-->
  <!--      </v-btn>-->
  <!--      <v-btn-->
  <!--        @click="$router.push({ name: 'cathedrals'})"-->
  <!--      >-->
  <!--        cathedrals-->
  <!--      </v-btn>-->
  <!--    </v-btn-group>-->
  <!--  </div>-->
</template>

<script>

import ManuscriptFullTitle from "@/components/manuscript/ManuscriptFullTitle.vue";
import ImgWithPlaceholder from "@/components/gallery/ImgWithPlaceholder.vue";
import { imgUrl, mainPages } from "@/utils/common";
import { useDisplay } from "vuetify";
import { api } from "@/services/api";
import DatePage from "@/components/pages/DatePage.vue";
import MainTitle from "@/components/common/title/MainTitle.vue";

export default {
  components: { MainTitle, DatePage, ImgWithPlaceholder, ManuscriptFullTitle },
  data() {
    return {
      mainData: {
        type: Object,
        required: true
      }
    };
  },
  computed: {
    mainPages() {
      return mainPages;
    }
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  mounted() {
    api
      .getMainData()
      .then((response) => (this.mainData = response.data));
  },
  methods: {
    imgUrl
  }
};
</script>
