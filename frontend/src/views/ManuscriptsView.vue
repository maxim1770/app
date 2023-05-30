<template>
  <div>
    <v-form>
      <v-container>
        <v-row class="justify-center">
          <v-col
            cols="12"
            md="6"
          >
            <v-text-field
              v-model="search"
              variant="solo"
              label="Поиск..."
              prepend-inner-icon="mdi-magnify"
              single-line
              clearable
            ></v-text-field>
          </v-col>
          <v-col
            cols="12"
            md="2"
          >
            <v-autocomplete
              label="Фонд"
              v-model="fund__title"
              :items="['Ф.304/I', 'Сол']"
              clearable
            ></v-autocomplete>
          </v-col>
          <v-col
            cols="12"
            md="2"
          >
            <v-switch
              v-model="order_by"
              color="success"
              label="Сортировать по почерку"
              value="-handwriting"
              hide-details
            ></v-switch>
          </v-col>
        </v-row>
        <v-row>
          <v-col
            cols="12"
            md="12"
            class="px-lg-12"
          >
            <v-range-slider
              v-model="yearsRange"
              :ticks="CENTURIES"
              min="1200"
              max="1597"
              :step="10"
              show-ticks="always"
              thumb-label="always"
              tick-size="5"
              class="align-center"
            >
            </v-range-slider>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
    <p v-if="!this.manuscripts.length" class="text-center">Список пуск</p>
    <div v-else class="d-block d-lg-flex flex-wrap justify-center">
      <v-card
        v-for="manuscript in this.manuscripts.items"
        :key="manuscript.id"
        class="mb-2 pa-2"
        :class="{ 'w-25 ma-5': xlAndUp }"
      >
        <v-img
          :src="manuscript.preview_img_path"
          height="500px"
          cover
        ></v-img>

        <v-card-text class="d-block">
          <p class="text-h6 text-center mb-2">{{ manuscript.title }}</p>
          <div class="text-end mb-1">
            <v-chip variant="tonal" color="cyan">{{ manuscript.year?.title }}</v-chip>
          </div>
          <div class="d-flex justify-space-between align-center">
            <b>Почерк:</b>
            <RatingHandwriting :manuscript="manuscript" />
          </div>

          <v-btn
            color="blue"
            @click="$router.push({ name: 'manuscript', params: { manuscriptCode: manuscript.code } })"
            class="ml-12"
          ></v-btn>

        </v-card-text>
      </v-card>
    </div>
  </div>
</template>

<script>
import { api } from "@/services/api";
import ManuscriptsPage from "@/components/pages/ManuscriptsPage.vue";
import { useDisplay } from "vuetify";
import RatingHandwriting from "@/components/manuscript/RatingHandwriting.vue";

export default {
  components: { RatingHandwriting, ManuscriptsPage },

  data() {
    return {
      manuscripts: {
        type: Object,
        required: true
      },
      search: this.$route.query.search,
      fund__title: this.$route.query.fund__title,
      yearsRange: [1200, 1597],
      order_by: []
    };
  },
  watch: {
    search() {
      this.routerManuscriptsPush();
    },
    fund__title() {
      this.routerManuscriptsPush();
    },
    yearsRange() {
      this.routerManuscriptsPush();
    },
    order_by() {
      this.routerManuscriptsPush();
    }
  },
  created() {
    this.CENTURIES = {
      1200: "1200",
      1250: "XIII",
      1300: "1300",
      1350: "XIV",
      1400: "1400",
      1450: "XV",
      1500: "1500",
      1550: "XVI",
      1597: "1597"
    };
    this.YEAR_CHRISTMAS = 5500;
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  mounted() {
    this.getManuscripts();
    if (this.$route.query.year__year__gte !== undefined) {
      this.yearsRange[0] = this.$route.query.year__year__gte - this.YEAR_CHRISTMAS;
    }
    if (this.$route.query.year__year__lt !== undefined) {
      this.yearsRange[1] = this.$route.query.year__year__lt - this.YEAR_CHRISTMAS;
    }
  },
  methods: {
    routerManuscriptsPush() {
      this.$router.push({
        name: "manuscripts", query: {
          search: (this.search !== null) ? this.search : undefined,
          fund__title: (this.fund__title !== null) ? this.fund__title : undefined,
          year__year__gte: (this.yearsRange[0] !== 1200) ? this.yearsRange[0] + this.YEAR_CHRISTMAS : undefined,
          year__year__lt: (this.yearsRange[1] !== 1597) ? this.yearsRange[1] + this.YEAR_CHRISTMAS : undefined,
          order_by: (this.order_by.length) ? this.order_by.join() : undefined
        }
      });
    },
    getManuscripts() {
      api.getManuscripts(
        {
          search: this.$route.query.search,
          fund__title: this.$route.query.fund__title,
          year__year__gte: this.$route.query.year__year__gte,
          year__year__lt: this.$route.query.year__year__lt,
          order_by: this.$route.query.order_by
        }
      ).then((response) => (this.manuscripts = response.data));
    }
  }
};
</script>
