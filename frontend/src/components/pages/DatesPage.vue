<template>
  <div>
    <FormDatesSearch
      @getItems="getDates"
      :year="$route.query.year"
      @update:search="replaceRouterQuery({year: $event})"
    />
    <DatesCalendar
      :dates="dates"
      :year="$route.query.year"
    />
    <ListSigns />
  </div>
</template>

<script>


import ListSigns from "@/components/dates/ListSigns.vue";
import FormDatesSearch from "@/components/dates/dates_search/FormDatesSearch.vue";
import { replaceRouterQuery } from "@/utils/common";
import DatesCalendar from "@/components/dates/DatesCalendar.vue";
import { api } from "@/services/api";

export default {
  components: { DatesCalendar, FormDatesSearch, ListSigns },
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
          // if (this.dates) {
          //   this.dates.attributes = this.dates.attributes?.concat(response.data.attributes);
          //   this.dates.dates = this.dates.dates?.concat(response.data.dates);
          // } else {
          this.dates = response.data;
          // }
        }
      );
    }
  }
};
</script>





