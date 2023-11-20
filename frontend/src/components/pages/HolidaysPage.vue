<template>
  <div>
    <FormHolidaysSearch
      @getItems="getHolidays"
      :holidaysSearchData="holidaysSearchData"
      :search="$route.query.search"
      :tipikon__title="$route.query.tipikon__title"
      :holiday_category__title="$route.query.holiday_category__title"
      :day__month="$route.query.day__month"
      :day__day="$route.query.day__day"
      @update:search="replaceRouterQuery( {search: $event})"
      @update:tipikon__title="replaceRouterQuery( {tipikon__title: $event})"
      @update:holiday_category__title="replaceRouterQuery( {holiday_category__title: $event})"
    />
    <NumItems :numItems="holidays.total" />
    <ListHolidays :holidays="holidays.items" :hasHeadTitle="false" />
  </div>
</template>

<script>


import { api } from "@/services/api";
import ListHolidays from "@/components/holiday/ListHolidays.vue";
import { replaceRouterQuery, scroll } from "@/utils/common";
import NumItems from "@/components/common/NumItems.vue";
import FormHolidaysSearch from "@/components/holiday/holidays_search/FormHolidaysSearch.vue";


export default {
  components: {
    FormHolidaysSearch,
    NumItems,
    ListHolidays
  },
  props: {
    holidaysSearchData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      holidays: {
        type: Object,
        required: true
      },
      page: {
        type: Number,
        required: true
      }
    };
  },
  computed: {
    apiGetHolidays() {
      return api.getHolidays({
        page: this.page,
        search: this.$route.query.search,
        tipikon__title: this.$route.query.tipikon__title,
        holiday_category__title: this.$route.query.holiday_category__title,
        day__month: this.$route.query.day__month,
        day__day: this.$route.query.day__day
      });
    }
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
      this.getHolidays();
    }
  },
  beforeMount() {
    this.getHolidays();
  },
  mounted() {
    scroll(this.getHolidaysPage);
  },
  methods: {
    replaceRouterQuery,
    getHolidaysPage() {
      this.page += 1;
      this.apiGetHolidays.then((response) => (this.holidays.items = this.holidays.items?.concat(response.data.items)));
    },
    getHolidays() {
      this.page = 1;
      this.apiGetHolidays.then((response) => (this.holidays = response.data));
    }
  }
};
</script>



