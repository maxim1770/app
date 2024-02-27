<template>
  <div>
    <v-card
      class="mb-2"
    >
      <MainTitle
        :title="$route.query.year"
        textColor="red-darken-3"
      />
    </v-card>
    <DatesCalendar
      v-if="$route.query.year"
      :dates="dates"
      :year="$route.query.year"
      @update:year="replaceRouterQuery({year: $event})"
    />
    <ListSigns />
  </div>
</template>

<script>


import ListSigns from "@/components/dates/ListSigns.vue";
import { replaceRouterQuery } from "@/utils/common";
import DatesCalendar from "@/components/dates/DatesCalendar.vue";
import { api } from "@/services/api";
import MainTitle from "@/components/common/title/MainTitle.vue";

export default {
  components: { MainTitle, DatesCalendar, ListSigns },
  data() {
    return {
      dates: {
        type: Object,
        required: true
      }
    };
  },
  computed: {
    apiGetDates() {
      return api.getDates({
        year: this.$route.query.year
      });
    }
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
      this.getDates();
    }
  },
  mounted() {
    this.getDates();
  },
  methods: {
    replaceRouterQuery,
    getDates() {
      this.apiGetDates.then(
        (response) => {
          this.dates = response.data;
          if (!this.$route.query.year) {
            this.replaceRouterQuery({ year: this.dates?.year });
          }
        }
      );
    }
  }
};
</script>
