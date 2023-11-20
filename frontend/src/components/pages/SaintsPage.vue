<template>
  <div>
    <FormSaintsSearch
      @getItems="getSaints"
      :saintsSearchData="saintsSearchData"
      :face_sanctity__title="$route.query.face_sanctity__title"
      :dignity__title="$route.query.dignity__title"
      :search="$route.query.search"
      @update:face_sanctity__title="replaceRouterQuery({face_sanctity__title: $event})"
      @update:dignity__title="replaceRouterQuery( {dignity__title: $event})"
      @update:search="replaceRouterQuery(  {search: $event})"
    />
    <NumItems :numItems="saints.total" />
    <ListSaints :saints="saints.items" />
  </div>
</template>


<script>
import { api } from "@/services/api";
import { replaceRouterQuery, scroll } from "@/utils/common";
import ListSaints from "@/components/saint/ListSaints.vue";
import FormSaintsSearch from "@/components/saint/saints_search/FormSaintsSearch.vue";
import NumItems from "@/components/common/NumItems.vue";

export default {
  components: { NumItems, FormSaintsSearch, ListSaints },
  props: {
    saintsSearchData: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      saints: {
        type: Object,
        required: true
      },
      page: {
        type: Number,
        required: true
      },
      order_by: [],
      selected_order_by: this.setSelectedOrderBy(this.$route.query.order_by)
    };
  },
  computed: {
    apiGetSaints() {
      return api.getSaints(
        {
          page: this.page,
          search: this.$route.query.search,
          face_sanctity__title: this.$route.query.face_sanctity__title,
          dignity__title: this.$route.query.dignity__title,
          order_by: this.$route.query.order_by
        }
      );
    }
  },
  watch: {
    "$route.query": function(newVal, oldVal) {
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
  beforeMount() {
    this.getSaints();
  },
  mounted() {
    scroll(this.getSaintsPage);
  },
  methods: {
    replaceRouterQuery,
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
    getSaintsPage() {
      this.page += 1;
      this.apiGetSaints.then((response) => {
        this.saints.items = this.saints.items?.concat(response.data.items);
      });
    },
    getSaints() {
      this.page = 1;
      this.apiGetSaints.then((response) => (this.saints = response.data));
    }
  }
};


</script>





