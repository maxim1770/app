<template>
  <div style="min-width: 1500px">
    <v-form>
      <v-container>
        <v-row class="justify-center">
          <v-col
            cols="12"
            md="4"
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
              label="Сан"
              v-model="face_sanctity__title"
              :items=saints.face_sanctity_titles
              clearable
            ></v-autocomplete>
          </v-col>
          <v-col
            cols="12"
            md="2"
          >
            <v-autocomplete
              label="Лик Святости"
              v-model="dignity__title"
              :items=saints.dignity_titles
              clearable
            ></v-autocomplete>
          </v-col>
          <v-col
            cols="12"
            md="3"
          >
            <v-autocomplete
              v-model="selected_order_by"
              label="Сортировать"
              :items=Object.keys(ORDER_BY_TITLES)
              multiple
              clearable
              chips
              variant="solo"
            ></v-autocomplete>
          </v-col>
          <v-col
            cols="12"
            md="1"
          >
            <v-btn
              @click="getSaints()"
              density="default" size="large" icon="mdi-magnify"
            ></v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>

    <v-list lines="two">
      <v-list-item
        v-for="saint in saints.saints"
        :key="saint.id"
        :title="saint.name"
        :to="{ name: 'saint', params: { saintSlug: saint.slug } }"
      >
        <v-list-item-subtitle>
          <v-chip v-if="saint.face_sanctity" class="ma-2" variant="tonal" color="green">
            {{ saint.face_sanctity.title }}
          </v-chip>
          <v-chip v-if="saint.dignity" class="ma-2" variant="tonal" color="blue">
            {{ saint.dignity.title }}
          </v-chip>
        </v-list-item-subtitle>
      </v-list-item>
    </v-list>

  </div>


</template>


<script>
import { api } from "@/services/api";
import { useDisplay } from "vuetify";

export default {

  data() {
    return {
      saints: {
        type: Object,
        required: true
      },
      search: this.$route.query.search,
      face_sanctity__title: this.$route.query.face_sanctity__title,
      dignity__title: this.$route.query.dignity__title,
      order_by: [],
      selected_order_by: this.setSelectedOrderBy(this.$route.query.order_by)
    };
  },
  watch: {
    search() {
      this.routerSaintsPush();
      this.getSaints();
    },
    face_sanctity__title() {
      this.routerSaintsPush();
      this.getSaints();
    },
    dignity__title() {
      this.routerSaintsPush();
      this.getSaints();
    },
    order_by() {
      this.routerSaintsPush();
      this.getSaints();
    },
    selected_order_by() {
      this.order_by = [];
      for (let value of this.selected_order_by) {
        this.order_by.push(this.ORDER_BY_TITLES[value]);
      }
    }
  },
  created() {
    this.ORDER_BY_TITLES = {
      "Имя": "name",
      "Лик Святости": "face_sanctity_id",
      "Сан": "dignity_id"
    };
  },
  setup() {
    const xlAndUp = useDisplay();
    return xlAndUp;
  },
  mounted() {
    this.getSaints();
  },
  methods: {
    setSelectedOrderBy(order_by_) {
      let selected_order_by_ = [];
      const ORDER_BY_TITLES = { // TODO: дублирование ORDER_BY_TITLES иначе пишет, что ORDER_BY_TITLES === undefined
        "Имя": "name",
        "Лик Святости": "face_sanctity_id",
        "Сан": "dignity_id"
      };
      if (order_by_) {
        for (let value of order_by_.split(",")) {
          selected_order_by_.push(Object.keys(ORDER_BY_TITLES).find(key => ORDER_BY_TITLES[key] === value));
        }
      }
      return selected_order_by_;
    },
    routerSaintsPush() {
      this.$router.push({
        name: "saints", query: {
          search: (this.search !== null) ? this.search : undefined,
          dignity__title: (this.dignity__title !== null) ? this.dignity__title : undefined,
          face_sanctity__title: (this.face_sanctity__title !== null) ? this.face_sanctity__title : undefined,
          order_by: (this.order_by.length) ? this.order_by.join() : undefined
        }
      });
    },
    getSaints() {
      api.getSaints(
        {
          search: this.$route.query.search,
          face_sanctity__title: this.$route.query.face_sanctity__title,
          dignity__title: this.$route.query.dignity__title,
          order_by: this.$route.query.order_by
        }
      ).then((response) => (this.saints = response.data));
    }
  }
};
</script>



